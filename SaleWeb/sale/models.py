from django.db import models

# Create your models here.

from django.db import models

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

class SKU(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.FloatField()
    owner = models.ForeignKey('auth.User', related_name="owner", on_delete=models.CASCADE)
    # photo = models.ImageField(blank=True, null=True, default=None, upload_to='products')

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