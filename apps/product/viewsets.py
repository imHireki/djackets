from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Product


class LatestProductsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()[0:4] 
    serializer_class = ProductSerializer
