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
    sku = ProductSerializer(many=False, read_only=True)
    sku_id = serializers.IntegerField(read_only=False)
    quantity = serializers.IntegerField(min_value=1, max_value=100)

    class Meta:
        model = Cart
        fields = '__all__'

    # def create(self, validated_data):
    #     buyer_data = validated_data.pop('buyer')
    #     buy = Buy.objects.create(**validated_data)
    #     Customer.objects.create(buyer=buyer, **buyer_data)
    #     return user

# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField(
#         max_length=100,
#         style={'placeholder': 'Email', 'autofocus': True}
#     )
#     password = serializers.CharField(
#         max_length=100,
#         style={'input_type': 'password', 'placeholder': 'Password'}
#     )
#     remember_me = serializers.BooleanField()