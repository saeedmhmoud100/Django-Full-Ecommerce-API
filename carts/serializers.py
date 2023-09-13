from rest_framework import serializers

from carts.models import Cart, CartItem, Coupon
from products.models import Image, Color, Product
from products.serializers import ProductSerializer


class CartItemsSerializer(serializers.ModelSerializer):
    product = ProductSerializer(Product)
    class Meta:
        model = CartItem
        fields = ['id','quantity','product','createdAt','updatedAt','_id']
        # fields = ['name']


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'
        # fields = ['name']


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemsSerializer(many=True, source='cartItems')
    coupon = CouponSerializer(Coupon)
    class Meta:
        model = Cart
        fields = ['id','total_price','coupon','cart_items','_id']

    # def get_cart_items(self,obj):
    #     return list(CartItemsSerializer(instance=obj.cartItems.all()).data)
