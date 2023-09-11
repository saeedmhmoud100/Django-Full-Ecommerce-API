from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from Utilities.Pagination import Pagination
from Utilities.permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from products.models import Product
from products.serializers import ProductSerializer


# Create your views here.

class ProductsView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = Pagination
    permission_classes = [IsOwnerOrReadOnly, IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        res = super().create(request, *args, **kwargs)
        colors = request.data.getlist('colors')
        images = request.data.getlist('images')

        if colors:
            product_data = res.data
            product = Product.objects.get(pk=product_data['id'])
            product.add_colors(colors)

        if images:
            product_data = res.data
            product = Product.objects.get(pk=product_data['id'])
            product.add_images(images)

        return res


class ProductDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = Pagination
    permission_classes = [IsOwnerOrReadOnly, IsAdminOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance=instance)
        return Response({'status': 'success'}, status=status.HTTP_200_OK)

