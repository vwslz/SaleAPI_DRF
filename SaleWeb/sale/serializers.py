from rest_framework import serializers
from sale.models import SKU, Customer, CartItem

class SKUSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length=100)
    # description = serializers.CharField(max_length=500)
    # price = serializers.DecimalField(
    #     min_value=1.00, max_value=100000,
    #     max_digits=None, decimal_places=2,
    # )
    buy = serializers.RelatedField(many=True, read_only=True)
    # photo = serializers.ImageField(default=None)

    # def get_cart_items(self, instance):
    #     items = CartItem.objects.filter(product=instance)
    #     return CartItemSerializer(items, many=True).data

    class Meta:
        model = SKU
        fields = ('id', 'name', 'description', 'price', 'price', 'buy',)

class CustomerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=20)
    name_first = serializers.CharField(max_length=50)
    name_last = serializers.CharField(max_length=50)
    buyer = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ('id', 'username', 'name_first', 'name_second', 'buyer',)

class CartItemsSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(min_value=1, max_value=100)
    customer = CustomerSerializer()
    sku = SKUSerializer()

    class Meta:
        model = CartItem
        fields = ('sku', 'quantity')