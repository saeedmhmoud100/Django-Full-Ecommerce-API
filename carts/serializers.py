from rest_framework import serializers

from carts.models import Cart, CartItem
from products.models import Image, Color, Product


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id','total_price','coupon']


class CartItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'
        # fields = ['name']
