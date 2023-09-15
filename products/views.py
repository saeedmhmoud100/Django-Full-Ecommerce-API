from django.db.models import Q
from django.http import Http404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from Utilities.Pagination import Pagination
from Utilities.permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly, IsStaffOrReadOnly, IsAdminOrOwnerOrReadOnly
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
    queryset = Product.objects.is_active()
    serializer_class = ProductSerializer
    pagination_class = Pagination
    permission_classes = [IsStaffOrReadOnly, IsAdminOrReadOnly]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        try:
            order = request.GET.get('sort')
            queryset = queryset.order_by(order)
        except:
            None

        try:
            search = request.GET.get('search')
            queryset = queryset.filter(Q(title__contains=search) | Q(description__contains=search))
        except:
            None

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        return Response({'status': 'not found'}, status=status.HTTP_404_NOT_FOUND)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, active=True)

    def create(self, request, *args, **kwargs):
        if 'imageCover' not in request.data:
            return Response({'imageCover': 'The image cover is required'},
                            status=status.HTTP_400_BAD_REQUEST)
        if 'title' not in request.data:
            return Response({'imageCover': 'The title is required'},
                            status=status.HTTP_400_BAD_REQUEST)
        res = super().create(request, *args, **kwargs)
        setImagesAndColors(request=request, res=res)
        return res


class ProductDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = Pagination
    permission_classes = [IsAdminOrOwnerOrReadOnly, IsAuthenticatedOrReadOnly]

    def get_object(self):
        res = super().get_object()
        if res.active or self.request.user.is_superuser or self.request.user == res.user:
            return res
        raise Http404("Product not found")

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


class LoggedUserProductsView(generics.ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = Pagination

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Product.objects.all()
        elif self.request.user.is_staff:
            return Product.objects.filter(user=self.request.user)
        else:
            return Product.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        return Response({'status': 'not found'}, status=status.HTTP_404_NOT_FOUND)
