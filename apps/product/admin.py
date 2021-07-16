# Django
from django.contrib import admin

# Models
from .models import Product, Category


# Register tables Product and Category on admin area
admin.site.register(Product)
admin.site.register(Category)
