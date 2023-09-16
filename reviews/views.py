from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response

from Utilities.Pagination import Pagination
from Utilities.permissions import IsNotAdmin, IsNotOwner, IsOwner, IsNotAdminOrReadOnly, IsOwnerOrReadOnly
from products.models import Product
from reviews.models import Reviews
from reviews.serializers import ReviewsSerializer


# Create your views here.


class GetReviews(generics.ListCreateAPIView):
    queryset = Reviews
    serializer_class = ReviewsSerializer
    pagination_class = Pagination
    permission_classes = [IsAuthenticatedOrReadOnly, IsNotAdminOrReadOnly, IsNotOwner]

    def get(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(pk=kwargs['pk'])
            reviews = Reviews.objects.filter(product=product)

            page = self.paginate_queryset(reviews)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
        except:
            return Response({'status': 'not found'}, status=status.HTTP_404_NOT_FOUND)

    def perform_create(self, serializer):
        if not Reviews.objects.filter(user=self.request.user,
                                      product=Product.objects.get(id=self.kwargs['pk'])).exists():
            serializer.save(user=self.request.user, product=Product.objects.get(id=self.kwargs['pk']))


class ChangeReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer

    permission_classes = [IsAuthenticatedOrReadOnly&IsOwnerOrReadOnly]
    # lookup_field = 'pk2'



    def get_object(self):
        pk2 = self.kwargs.get('pk2')
        review = get_object_or_404(self.queryset, pk=pk2)
        self.check_object_permissions(self.request,review)
        return review
