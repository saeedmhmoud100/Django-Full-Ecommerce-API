from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import generics

from Utilities.Pagination import Pagination
from Utilities.permissions import IsAdmin
from users_admin.serializers import UsersAdminSerializer


# Create your views here.
class GetAllUsers(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UsersAdminSerializer
    permission_classes = [IsAdmin]
    pagination_class = Pagination