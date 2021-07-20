"""
URL settings for product app
"""

# Django
from django.urls import path, include

# Django Rest Framework
from rest_framework.routers import DefaultRouter

# Product app
from . import viewsets


router = DefaultRouter()
router.register(r'products', viewsets.ProductListDetail)
 
urlpatterns = router.urls

urlpatterns += [
    path('products/<slug:category_slug>/<slug:product_slug>/',
    viewsets.ProductDetail.as_view())
]
