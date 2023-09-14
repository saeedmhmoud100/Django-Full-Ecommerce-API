from django.contrib.auth import get_user_model
from rest_framework import serializers

from brands.models import Brand
from products.models import Product
from products.serializers import ProductSerializer
from users.models import MyUser


class UsersAdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = "__all__"
