from email.headerregistry import Address

from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from Utilities.Pagination import Pagination
from Utilities.permissions import  IsAdminOrNotStaff
from carts.models import Cart
from orders.models import Order
from orders.serializers import OrderSerializer
from users.models import UserAddress


class GetCreatOrders(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = Pagination
    permission_classes = [IsAuthenticated & IsAdminOrNotStaff]


    def create(self, request, *args, **kwargs):
        data = request.data
        ser = OrderSerializer(data=data)

        if request.user.is_superuser:
            return Response({'status':'fail','msg':'you are not allowed to perform this action'})

        try:
            address = UserAddress.objects.get(pk=data['address'],user=request.user)
        except:
            return Response({'status':'fail','msg':'error in address'},status=status.HTTP_400_BAD_REQUEST)
        try:
            cart = Cart.objects.get(user=request.user)
        except:
            return Response({'status':'fail'})
        if not cart.cartItems.exists():
            return Response({'status':'fail','msg':'cart is empty'},status=status.HTTP_400_BAD_REQUEST)

        if ser.is_valid(raise_exception=True):
            user = get_user_model().objects.get(id=request.user.id)
            # new_cart = Cart(user_id=request.user.id)
            # new_cart.save()
            cart.user=None
            cart.save()
            ser.save(address=address,user=user,cart=cart,total_order_price=cart.total_price)
            # Cart.objects.create(user=user)
            # user.cart = new_cart
            # user.save()
            return Response({'status':'success','data':ser.data},status=status.HTTP_201_CREATED)
        return Response({'status':'fail'},status=status.HTTP_400_BAD_REQUEST)

    # def perform_create(self, serializer):
    #     print(self.request.data)