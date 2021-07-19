from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'url',
            
            'id',
            'name',
            'description',
            'price',
            'category',

            'get_category_name',
            'get_absolute_url',
            'get_image',
            'get_thumbnail',
        ]
