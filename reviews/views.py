from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from Utilities.Pagination import Pagination
from products.models import Product
from reviews.models import Reviews
from reviews.serializers import ReviewsSerializer


# Create your views here.


class GetReviews(generics.ListCreateAPIView):
    queryset = Reviews
    serializer_class = ReviewsSerializer
    pagination_class = Pagination
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        try:
            product= Product.objects.get(pk=kwargs['pk'])
            reviews = Reviews.objects.filter(product=product)

            page = self.paginate_queryset(reviews)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
        except:
            return Response({'status': 'not found'}, status=status.HTTP_404_NOT_FOUND)

