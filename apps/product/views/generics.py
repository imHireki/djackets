"""
Views for product app's serializers
"""

# Django
from django.shortcuts import get_object_or_404

# Django Rest Framework
from rest_framework import generics, exceptions, status
from rest_framework.response import Response

# Product app
from ..serializers import ProductSerializer, CategorySerializer
from ..models import Product, Category


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


class Cart(generics.ListAPIView):
    """
    Cart based on session
    """
    def list(self, *args, **kwargs):
        cart = self.get_cart()
        if not cart:
            raise exceptions.NotFound("cart is empty")

        return Response(cart, status.HTTP_200_OK)

    def get_cart(self):
        """ Get cart from session"""
        return self.request.session.get('cart')
