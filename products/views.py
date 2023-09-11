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
    permission_classes = [IsOwnerOrReadOnly, IsAdminOrReadOnly]

    # def create(self, request, *args, **kwargs):
    #     # Ensure 'owner' field is set to the currently authenticated user
    #
    #     # Use the serializer to validate and save the data
    #     request.data.user = request.user.id
    #     serializer = self.get_serializer(data=request.data,context={'request': request})
    #     serializer.is_valid(raise_exception=True)
    #     # serializer.data['owner'] = request.user.id
    #     serializer.save(user=request.data.user)
    #
    #     return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        # Set the 'owner' field to the currently authenticated user
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
