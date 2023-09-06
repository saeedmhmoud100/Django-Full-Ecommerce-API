from rest_framework import viewsets, routers
from Utilities.permissions import IsAdminOrReadOnly
from brands.models import Brand
from brands.serializers import BrandSerializer


# Create your views here.


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAdminOrReadOnly]


router = routers.DefaultRouter()
router.register(r'brand', BrandViewSet)
