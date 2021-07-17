from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'get_absolute_url',
            'get_image',
            'get_thumbnail',
        ]
