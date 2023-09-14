from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from Utilities.Pagination import Pagination
from Utilities.permissions import IsAdmin
from products.models import Product
from users.serializers import UserWishListSerializer, UserSerializer


# Create your views here.


class LoggedUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user


    def update(self, request, *args, **kwargs):
        user = self.get_object()
        new_password = request.data.get('password')

        ser = UserSerializer(instance=request.user,data=request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            if new_password:
                user.set_password(new_password)
                user.save()

        return Response({"status": "success",'data':UserSerializer(instance=self.get_object()).data}, status=status.HTTP_200_OK)





class WishList(APIView):
    serializer_class = UserWishListSerializer
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        queryset = get_user_model().objects.filter(pk=self.request.user.id)
        if queryset:
            return Response(UserWishListSerializer(instance=queryset, many=True).data[0])
        return Response({'status': 'not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def wishlistChange(request, pk):
    try:
        user = get_user_model().objects.get(pk=request.user.pk)
        if request.method == 'POST':
            Product.objects.get(pk=pk).users_wishlist.add(user)
        elif request.method == 'DELETE':
            Product.objects.get(pk=pk).users_wishlist.remove(user)
        return Response({'status': 'success', 'data': UserWishListSerializer(instance=user).data},
                        status=status.HTTP_200_OK)
    except:
        return Response({'status': 'fail'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def clearWishlist(request):
    try:
        if request.method == 'DELETE':
            user = get_user_model().objects.get(pk=request.user.pk)
            user.wishlist.clear()
            return Response({'status': 'success', 'data': UserWishListSerializer(instance=user).data},
                            status=status.HTTP_200_OK)
    except:
        return Response({'status': 'fail'}, status=status.HTTP_400_BAD_REQUEST)

