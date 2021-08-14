"""
Views for product app's serializers
"""

# Django
from django.db.models.query_utils import Q
from django.shortcuts import get_object_or_404

# Django Rest Framework
from rest_framework import generics, exceptions, status
from rest_framework.views import APIView
from rest_framework.response import Response

# Product app
from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category


class LatestProducts(APIView):
    """
    Latest Products

    Return a Response with a `serialized queryset`
    """
    def get(self, *args, **kwargs):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


# class LatestProducts(generics.ListAPIView):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()[0:4]


class ProductDetail(APIView):
    """
    Detail for a Product object

    Return Response with a `serialized object`
    """
    def get(self, request, category_slug, product_slug):
        product = get_object_or_404(
            Product,
            category__slug=category_slug,
            slug=product_slug
        )
        serializer = ProductSerializer(product)
        return Response(serializer.data)


# class ProductDetail(generics.RetrieveAPIView):
#     serializer_class = ProductSerializer

#     def retrieve(self, request, category_slug, product_slug):
#         obj = get_object_or_404(
#             Product,
#             category__slug=category_slug,
#             slug=product_slug
#         )
#         serializer = self.get_serializer(obj)
#         return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryDetail(APIView):
    """
    Detail for a Category object

    Return a Response with the `serialized obejct`
    """
    def get(self, request, category_slug):
        category = get_object_or_404(
            Category,
            slug=category_slug
        )
        serializer = CategorySerializer(category)
        return Response(serializer.data)


# class CategoryDetail(generics.RetrieveAPIView):
#     serializer_class = CategorySerializer

#     def retrieve(self, request, category_slug):
#         obj = get_object_or_404(Category, slug=category_slug)
#         serializer = self.get_serializer(obj)
#         return Response(serializer.data)


class SearchProducts(APIView):
    """
    Search funcion that receives a GET with a `query` string

    Return a Response with the `serialized queryset`
    """
    def post(self, *args, **kwargs):
        queryset, query = self.get_queryset()
        if not queryset or not query:
            # raise exceptions.NotFound
            return Response({"products":[]}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        query = self.request.data.get('query', '')
        queryset = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        return queryset, query
