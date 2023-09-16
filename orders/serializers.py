from rest_framework import serializers

from carts.serializers import CartSerializer
from orders.models import Order
from users.serializers import UserAddressesSerializer, UserSerializer


class OrderSerializer(serializers.ModelSerializer):
    address = UserAddressesSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    cart = CartSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'