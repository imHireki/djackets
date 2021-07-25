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
    """
    Product List

    Return a Response with a `serialized queryset`
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()[0:4]


class ProductDetail(generics.RetrieveAPIView):
    """
    Detail for a Product object

    Return Response with a `serialized object`
    """
    serializer_class = ProductSerializer

    def retrieve(self, request, category_slug, product_slug):
        obj = get_object_or_404(
            Product,
            category__slug=category_slug,
            slug=product_slug
        )
        serializer = self.get_serializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryDetail(generics.RetrieveAPIView):
    """
    Detail for a Category object

    Return a Response with the `serialized obejct`
    """
    serializer_class = CategorySerializer

    def retrieve(self, request, category_slug):
        obj = get_object_or_404(Category, slug=category_slug)
        serializer = self.get_serializer(obj)
        return Response(serializer.data)


class Search(views.APIView):
    """
    Search funcion that receives a POST with a `query` string

    Return a Response with the `serialized queryset`
    """
    def post(self, request):
        queryset, query = self.get_queryset(request)

        if not queryset or not query:
            return Response([], status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def get_queryset(self, request):
        query = request.data.get('query', '')

        queryset = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        return queryset, query
