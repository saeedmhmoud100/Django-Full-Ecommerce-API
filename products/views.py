from rest_framework import generics, status
from rest_framework.response import Response

from Utilities.Pagination import Pagination
from Utilities.permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from products.models import Product
from products.serializers import ProductSerializer


# Create your views here.

class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = Pagination
    permission_classes = [IsOwnerOrReadOnly,IsAdminOrReadOnly]
