from rest_framework import viewsets, routers
from brands.models import Brand
from brands.serializers import BrandSerializer


# Create your views here.


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


router = routers.DefaultRouter()
router.register(r'brand', BrandViewSet)
