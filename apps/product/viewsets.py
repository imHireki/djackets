from rest_framework import viewsets, views, generics
from .serializers import ProductSerializer
from .models import Product


class ProductListDetail(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
