"""
Serializers for product app's models

ProductSerializer for Product model
CategorySerializer for Category model
"""

# Rest Framework
from rest_framework import serializers

# Product app
from .models import Product, Category


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
            'get_absolute_url',
            'description',
            'price',
            # 'category',
            'get_image',
            'get_thumbnail',
        ]

class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for Category Model
    """
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'get_absolute_url',
            'products'
        ]
