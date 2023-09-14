from rest_framework import serializers

from carts.models import Cart, CartItem
from coupons.models import Coupon
from coupons.serializers import CouponSerializer
from products.models import Image, Color, Product
from products.serializers import ProductSerializer, ColorSerializer


class CartItemsSerializer(serializers.ModelSerializer):
    product = ProductSerializer(Product)
    color = ColorSerializer(Color)
    class Meta:
        model = CartItem
        fields = ['id','quantity','color','product','createdAt','updatedAt','_id']
        # fields = ['name']


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemsSerializer(many=True, source='cartItems')
    coupon = CouponSerializer(Coupon)
    class Meta:
        model = Cart
        fields = ['id','total_price','coupon','cart_items','_id']

    def get_color(self,obj):
        return obj.name

    # def get_cart_items(self,obj):
    #     return list(CartItemsSerializer(instance=obj.cartItems.all()).data)
