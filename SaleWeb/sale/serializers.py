from rest_framework import serializers
from sale.models import SKU, Customer, CartItem

from django.contrib.auth.models import User

class SKUSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = SKU
        fields = ('id', 'name', 'description', 'price', 'price', 'owner')


class UserSerializer(serializers.ModelSerializer):
    # sku = serializers.HyperlinkedRelatedField(many=True, view_name='skus-detail', read_only=True)
    #
    # class Meta:
    #     model = User
    #     fields = ['id', 'username', 'sku']

    class Meta:
        model = User
        fields = ['id', 'username',]

class CustomerSerializer(serializers.ModelSerializer):
    sku = serializers.PrimaryKeyRelatedField(many=True, queryset=SKU.objects.all())
    # filter(
    #     first_name__startswith='R'
    # ).only("first_name", "last_name"))
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