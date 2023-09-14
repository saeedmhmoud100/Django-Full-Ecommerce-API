from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, PermissionsMixin
from rest_framework import serializers

from brands.models import Brand
from products.models import Product
from products.serializers import ProductSerializer
from users.models import MyUser


class UsersAdminSerializer(serializers.ModelSerializer):
    groups = serializers.ModelSerializer(Group,many=True,read_only=True)
    user_permissions = serializers.ModelSerializer(PermissionsMixin,many=True,read_only=True)
    class Meta:
        model = get_user_model()
        fields = "__all__"
        execute = ('groups', 'user_permissions')
