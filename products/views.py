from rest_framework import generics, status
from rest_framework.response import Response

from Utilities.Pagination import Pagination
from Utilities.permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from products.models import Product
from products.serializers import ProductSerializer


# Create your views here.


def setImagesAndColors(request, res):
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


class ProductsView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = Pagination
    permission_classes = [IsOwnerOrReadOnly, IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        if 'imageCover' not in request.data:
            return Response({'imageCover': 'The image cover is required'},
                            status=status.HTTP_400_BAD_REQUEST)
        res = super().create(request, *args, **kwargs)
        setImagesAndColors(request=request, res=res)
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

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        res = super().update(request, *args, **kwargs)
        if not partial or len(request.data.getlist('images')) > 0:
            self.get_object().delete_images()
        if not partial or len(request.data.getlist('colors')):
            self.get_object().delete_colors()
        setImagesAndColors(res=res, request=request)

        return Response({'status': 'success', 'data': ProductSerializer(self.get_object()).data},
                        status=status.HTTP_200_OK)
