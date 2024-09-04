from django.contrib.auth import get_user_model
from rest_framework import serializers

from brands.models import Brand
from products.models import Product
from products.serializers import ProductSerializer
from users.models import MyUser, UserAddress


class UserAddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        # fields = '__all__'
        exclude = ('user',)


class UserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True)
    is_active = serializers.BooleanField(read_only=True)
    is_staff = serializers.BooleanField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
    wishlist = serializers.SerializerMethodField()
    addresses=UserAddressesSerializer(UserAddress,many=True,required=False)
    class Meta:
        model = get_user_model()
        fields = ['id','username','first_name','last_name','email','is_active','is_staff','is_superuser','password', 'addresses','wishlist']

    def get_wishlist(self, obj):
        return ProductSerializer(obj.wishlist.all(), many=True).data

class UserSerializer2(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True)
    is_active = serializers.BooleanField(read_only=True)
    is_staff = serializers.BooleanField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
    class Meta:
        model = get_user_model()
        fields = ['id','username','first_name','last_name','email','is_active','is_staff','is_superuser']


class UserWishListSerializer(serializers.ModelSerializer):
    wishlist = serializers.SerializerMethodField()

    # product = ProductSerializer(Product)
    class Meta:
        model = MyUser
        fields = ['wishlist']

    def get_wishlist(self, obj):
        return ProductSerializer(obj.wishlist.all(), many=True).data
