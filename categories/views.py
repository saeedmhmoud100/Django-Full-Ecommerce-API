from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from Utilities.Pagination import Pagination
from Utilities.permissions import IsAdminOrReadOnly
from categories.models import Category
from categories.serializers import CategorySerializer


class CategoryListCreateViewAPI(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = Pagination
    # authentication_classes = [TokenAuthentication]

    def post(self, request, *args, **kwargs):
        print(request.data)
        if not request.data.get('image'):
            return Response({'image':'this field is required'})
        return super().post(request,*args,**kwargs)

