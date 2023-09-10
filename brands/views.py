from rest_framework import viewsets, routers
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from Utilities.Pagination import Pagination
from Utilities.permissions import IsAdminOrReadOnly
from brands.models import Brand
from brands.serializers import BrandSerializer


# Create your views here.



class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = Pagination
    # authentication_classes = [JSONWebTokenAuthentication]

router = routers.DefaultRouter()
router.register(r'brands', BrandViewSet)
