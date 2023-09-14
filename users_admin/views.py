from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password,check_password
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from Utilities.Pagination import Pagination
from Utilities.permissions import IsAdmin
from users_admin.serializers import UsersAdminSerializer


# Create your views here.
class GetAllUsers(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UsersAdminSerializer
    permission_classes = [IsAdmin]
    pagination_class = Pagination


class UsersChange(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UsersAdminSerializer
    permission_classes = [IsAdmin]

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        new_password = request.data.get('password')

        if not new_password:
            return Response({"error": "New password is required"}, status=status.HTTP_400_BAD_REQUEST)

        user.password = make_password(new_password)
        user.save()

        return Response({"status": "success",'data':UsersAdminSerializer(instance=self.get_object()).data}, status=status.HTTP_200_OK)