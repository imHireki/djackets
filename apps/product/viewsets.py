"""
Viewsets for product app's serializers

"""

# Django
from django.shortcuts import get_object_or_404

# Rest
from rest_framework import serializers, viewsets, views, generics
from rest_framework.response import Response

# Product app
from .serializers import ProductSerializer
from .models import Product


class ProductListDetail(viewsets.GenericViewSet, generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        self.queryset = Product.objects.filter()
        return self.queryset


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer

    def get_object(self, category_slug, product_slug):
        return get_object_or_404(
            Product,
            category__slug=category_slug,
            slug=product_slug
        )
    
    def get(self, request, category_slug, product_slug):
        obj = self.get_object(category_slug, product_slug)
        serializer = self.serializer_class(obj)
        return Response(serializer.data)
