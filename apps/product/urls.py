"""
URL settings for product app
"""

# Django
from django.urls import path, include

# Django Rest Framework
from rest_framework.routers import DefaultRouter

# Product app
from . import viewsets


# Registering routing to Lists
router = DefaultRouter()
router.register(r'products', viewsets.ProductList)
router.register(r'categories', viewsets.CategoryList)

# Routing Lists
urlpatterns = router.urls

# Routing Details
urlpatterns += [
    path(
        'products/<slug:category_slug>/<slug:product_slug>/',
        viewsets.ProductDetail.as_view()
    ),
    path(
        'products/<slug:category_slug>/',
        viewsets.CategoryDetail.as_view()
    ),
    path(
        'products/search/', viewsets.search
    ),
]
