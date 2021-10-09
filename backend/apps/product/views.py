from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ProductSerializer
from .models import Product, Category


class LatestProductList(APIView):
    def get(self, *args, **kwargs):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        serializer.is_valid(raise_exception=True)
        return response(serializer.data)

