from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from carts.models import Cart
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

    return Response({})

