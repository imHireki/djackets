from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ProductSerializer
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

