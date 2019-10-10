from rest_framework import serializers
from sale.models import SKU, Customer, CartItem

class SKUSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = ('id', 'name', 'description', 'price', 'price',)

class CustomerSerializer(serializers.ModelSerializer):
    buy = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ('id', 'username', 'name_first', 'name_last', 'buy',)

class CartItemsSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(min_value=1, max_value=100)
    customer = CustomerSerializer()
    sku = SKUSerializer()

    class Meta:
        model = CartItem
        fields = ('sku', 'quantity')