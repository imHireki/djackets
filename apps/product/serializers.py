"""
Serializers for product app's models

ProductSerializer for Product model
CategorySerializer for Category model
"""

# Rest Framework
from rest_framework import serializers

# Product app
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Product model
    """
    class Meta:
        model = Product
        fields = [
            'get_obj_url',
            'id',
            'name',
            'description',
            'price',
            'category',
            'get_absolute_url',
            'get_image',
            'get_thumbnail',
        ]
