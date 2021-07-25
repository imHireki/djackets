"""
Viewsets for product app's serializers

"""

# Django
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Django Rest Framework
from rest_framework import viewsets, generics, views
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.serializers import Serializer

# Product app
from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category


class ProductList(generics.ListAPIView):
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

    def get(self, request, category_slug):
        obj = self.get_object(category_slug)
        serializer = self.serializer_class(obj)
        return Response(serializer.data)


class Search(generics.CreateAPIView):
    serializer_class = ProductSerializer
    
    def create(self, request):
        """
        Receive a POST request, try find related objects in db
        return 'em as serialized objects
        """
        query = self.request.data.get('query', '')

        if not query:
            return Response({'products': ''}, status.HTTP_204_NO_CONTENT)
        
        queryset = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        serializer = self.get_serializer(queryset, many=True)
        
        return Response(serializer.data, status.HTTP_201_CREATED)
