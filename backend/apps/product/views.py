from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ProductSerializer
from .models import Product, Category


class LatestProductList(APIView):
    def get(self, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(data=products, many=True)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

