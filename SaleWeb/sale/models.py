from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class Product(models.Model):
    sku = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.FloatField()
    # owner = models.ForeignKey('auth.User', related_name="owner", on_delete=models.CASCADE)
    # photo = models.ImageField(blank=True, null=True, default=None, upload_to='products')

class Customer(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

class Cart(models.Model):
    # buyer = models.ForeignKey('auth.User', related_name='buyer', on_delete=models.CASCADE)
    buyer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    unique_together = (("buyer", "product"),)