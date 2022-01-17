from django.urls import path
from . import views

'''
List of urls for the website
'''
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('create_item', views.create_item, name='create_item'),
    path('edit/<str:pk>', views.edit, name='edit'),
    path('edit_item', views.edit_item, name='edit_item'),
    path('delete', views.delete, name='delete'),
    path('export_csv', views.export_csv, name='export_csv')
]