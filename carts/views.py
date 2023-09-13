from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from Utilities.permissions import IsNotAdmin
from carts.models import Cart, CartItem
from carts.serializers import CartSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def cart(request):
    if request.method == 'GET' and request.user.is_authenticated and not request.user.is_superuser:
        if Cart.objects.filter(user=request.user).exists():
            data = CartSerializer(instance=Cart.objects.filter(user=request.user).first())
            return Response(data.data)
        else:
            Cart.objects.create(user=request.user)

    return Response({}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def cartChange(request, pk):
    if request.method == 'POST' and not request.user.is_superuser:
        cartItem = request.user.cart.cartItems.filter(product_id=pk)
        if cartItem.exists():
            cartItem.delete()
        else:
            CartItem.objects.create(cart=request.user.cart, product_id=pk)
        return Response(CartSerializer(instance=request.user.cart).data,status=status.HTTP_200_OK)
    return Response({}, status=status.HTTP_400_BAD_REQUEST)
