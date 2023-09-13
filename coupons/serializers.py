from rest_framework import serializers

from carts.models import Coupon



class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'
        # fields = ['name']