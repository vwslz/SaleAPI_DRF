from rest_framework import serializers
from sale.models import Product, Customer, Cart
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class ProductSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Product
        fields = ('id', 'sku', 'name', 'description', 'price',)

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'firstname', 'lastname')

class CartSerializer(serializers.ModelSerializer):
    buyer = CustomerSerializer(many=False, read_only=True)
    buyer_id = serializers.IntegerField(read_only=False)
    product = ProductSerializer(many=False, read_only=True)
    product_id = serializers.IntegerField(read_only=False)
    quantity = serializers.IntegerField(min_value=1, max_value=100)

    class Meta:
        model = Cart
        fields = '__all__'