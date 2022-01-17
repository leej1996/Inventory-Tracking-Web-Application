from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
import csv
from .models import Item


# Create your views here.
def index(request):
    '''
    Main page
    '''
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})


def create(request):
    '''
    page for user to enter information for the creation of a new item
    '''
    return render(request, 'create.html')


def create_item(request):
    '''
    Takes information from user and creates a new item in the model (database)
    '''
    if request.method == "GET":
        name = request.GET['name']
        type = request.GET['type']
        quantity = request.GET['quantity']
        price = request.GET['price']

        item = Item.objects.create_item(name=name, type=type, quantity=quantity, price=price)
        item.save()
        messages.info(request, 'Item created successfully!')
        return redirect('/')
    else:
        return render(request, 'create.html')


def edit(request, pk):
    '''
    Page to get information from user about what to edit
    '''
    item = Item.objects.get(id=pk)
    return render(request, 'edit.html', {'item': item})


def edit_item(request):
    '''
    Takes inputs from user and updates the item in the model (database)
    '''
    if request.method == "GET":
        name = request.GET['name']
        type = request.GET['type']
        quantity = request.GET['quantity']
        price = request.GET['price']
        item_id = request.GET['item_id']
        if not name or not type or not quantity or not price:
            '''
            Check if any of the fields were empty
            '''
            messages.info(request, 'One of your fields is empty. Please input a value for all fields.')
            return_url = 'edit/' + item_id
            return redirect(return_url)
        else:
            '''
            Update the item with new info
            '''
            item = Item.objects.get(id=item_id)
            item.name = name
            item.type = type
            item.quantity = quantity
            item.price = price
            item.save()
            messages.info(request, 'Item edited successfully')
            return redirect('/')


def delete(request):
    '''
    Deletes item from the model (database)
    '''
    if request.method == "GET":
        item_id = request.GET['item_id']
        item = Item.objects.get(id=item_id)
        item.delete()
        messages.info(request, 'Item deleted!')
        return redirect('/')
    else:
        return render(request, "index.html")


def export_csv(request):
    '''
    Exports the model (database) as a downloadable CSV file
    '''
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="inventory.csv"'}
    )
    writer = csv.writer(response)
    items = Item.objects.all()
    writer.writerow(['ID', 'Name', 'Type', 'Quantity', 'Price', 'Date last stocked'])
    for item in items:
        writer.writerow([item.id, item.name, item.type, item.quantity, item.price, item.created_on])

    return response
