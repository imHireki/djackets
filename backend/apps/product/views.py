from django.http import Http404
from django.db.models import Q

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category


class LatestProductList(APIView):
    def get(self, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(
                category__slug=category_slug
            ).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404
 
    def get(self, request, category_slug, product_slug, *args, **kwargs):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, *args, **kwargs):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


class Search(APIView):
    def post(self, *args, **kwargs):
        query = self.request.data.get('query', '')

        if query:
            products = Product.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)

        else:
            return Response({"products": []})

