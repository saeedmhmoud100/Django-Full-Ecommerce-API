from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from carts.models import Cart, CartItem
from carts.serializers import CartSerializer, CartItemsSerializer
from products.models import Color


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


@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def cartItemsChange(request, pk):
    if not request.user.is_superuser:
        if request.method == 'POST':
            # try:
                color_name = request.data.get('color')
                color = None
                if color_name and Color.objects.filter(product_id=pk, name=color_name).exists():
                    color = Color.objects.get(product_id=pk, name=color_name)
                c, t = CartItem.objects.get_or_create(cart=request.user.cart, product_id=pk, color=color)

                return Response({'status': 'success', 'data': CartSerializer(instance=request.user.cart).data},
                                status=status.HTTP_200_OK)

            # except:
            #     return Response({'status': 'fail'}, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            try:
                CartItem.objects.filter(product_id=pk).delete()
                return Response({'status': 'success', 'data': CartSerializer(instance=request.user.cart).data},
                                status=status.HTTP_200_OK)
            except:
                pass

    return Response({}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateCartItemCount(request, pk, *args, **kwargs):
    if request.method == 'POST' and not request.user.is_superuser:
        try:
            cartItem = request.user.cart.cartItems.get(pk=pk)
            cartItem.quantity = request.data.get('quantity')
            cartItem.save()
            return Response({'status': 'success', 'data': CartItemsSerializer(instance=cartItem).data},
                            status=status.HTTP_200_OK)
        except CartItem.DoesNotExist:
            return Response({'status': "fail", 'msg': 'Cart item not found '}, status=status.HTTP_404_NOT_FOUND)
    return Response({}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def clearCart(request):
    if not request.user.is_superuser:
        if request.method == 'DELETE':
            request.user.cart.cartItems.all().delete()
            return Response({'status': 'success', 'data': CartSerializer(instance=request.user.cart).data},
                            status=status.HTTP_200_OK)
    return Response({}, status=status.HTTP_400_BAD_REQUEST)
