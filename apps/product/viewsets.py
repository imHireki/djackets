"""
Viewsets for product app's serializers

"""

# Django
from django.shortcuts import get_object_or_404

# Django Rest Framework
from rest_framework import viewsets, generics
from rest_framework.response import Response

# Product app
from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category


class ProductList(generics.ListAPIView, viewsets.GenericViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()[0:4]


class ProductDetail(generics.RetrieveAPIView):
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


class CategoryDetail(generics.RetrieveAPIView):
    serializer_class = CategorySerializer

    def get_object(self, category_slug):
        return get_object_or_404(
            Category,
            slug=category_slug
        )

    def get(self, request, category_slug, *args, **kwargs):
        obj = self.get_object(category_slug)
        serializer = self.serializer_class(obj)
        return Response(serializer.data)
