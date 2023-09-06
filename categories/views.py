from rest_framework import generics, status
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
            return Response({'image': 'this field is required'})
        return super().post(request, *args, **kwargs)


class CategoryRetrieveUpdateDestroyViewAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

    # authentication_classes = [TokenAuthentication]
    def partial_update(self, request, *args, **kwargs):
        print(request.data)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print("Object Updated Successfully:", serializer.data)  # Log the updated data
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'status':'success'}, status=status.HTTP_204_NO_CONTENT)
