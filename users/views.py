from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Utilities.Pagination import Pagination
from Utilities.permissions import IsNotAdmin
from users.models import MyUser
from users.serializers import UserWishListSerializer


# Create your views here.


class WishList(APIView):
    serializer_class = UserWishListSerializer
    permission_classes = [IsAuthenticated]

    def get(self,*args,**kwargs):
        queryset = get_user_model().objects.filter(pk=self.request.user.id)
        if queryset:
            return Response(UserWishListSerializer(instance=queryset,many=True).data[0])
        return Response({'status': 'not found'}, status=status.HTTP_404_NOT_FOUND)