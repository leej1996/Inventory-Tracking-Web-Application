from django.db import models


# Create your models here.

class ItemManager(models.Manager):
    '''
    Used for instantiation of item objects
    '''
    def create_item(self, name, type, quantity, price):
        item = self.create(name=name, type=type, quantity=quantity, price=price)
        return item


class Item(models.Model):
    '''
    Represents an inventory item in the system
    '''
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    created_on = models.DateTimeField(auto_now_add=True)

    objects = ItemManager()
