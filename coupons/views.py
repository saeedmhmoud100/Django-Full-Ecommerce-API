from django.shortcuts import render
from rest_framework import viewsets, routers
from rest_framework.permissions import IsAdminUser

from Utilities.Pagination import Pagination
from coupons.models import Coupon
from coupons.serializers import CouponSerializer


# Create your views here.


class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = [IsAdminUser]
    pagination_class = Pagination
    lookup_field = 'name'
    # authentication_classes = [JSONWebTokenAuthentication]

router = routers.DefaultRouter()
router.register(r'', CouponViewSet)
