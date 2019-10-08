from django.db import models

# Create your models here.

from django.db import models

class SKU(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.FloatField()
    # photo = models.ImageField(blank=True, null=True, default=None, upload_to='products')

    # class Meta:
    #     ordering = ['created']
    # class Meta:
    #     ordering = ['created']

class Customer(models.Model):
    username = models.CharField(max_length=20, blank=True, default='')
    name_first = models.CharField(max_length=50, blank=True, default='')
    name_last = models.CharField(max_length=50, blank=True, default='')

class CartItem(models.Model):
    customer = models.ForeignKey(Customer, related_name='buyer', on_delete=models.CASCADE)
    sku = models.ForeignKey(SKU, related_name='buy', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    # class Meta:
    #     model = CartItem
    #     fields = ('product', 'quantity')