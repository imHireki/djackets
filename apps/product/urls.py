"""
URL settings for product app
"""

# Django
from django.urls import path

# Django Rest Framework
from rest_framework.routers import DefaultRouter

# Product app
from . import viewsets


urlpatterns = [
    # NOTE: Careful when dealing with URLs alike each other
    # To reference the static URL before the one with a slug.
    path(
        'products/Search/',
        viewsets.Search.as_view()
    ),
    path(
        'products/AddToCart/',
        viewsets.AddToCart.as_view()
    ),
    path(
        'products/RemoveFromCart/',
        viewsets.RemoveFromCart.as_view()
    ),

    # URLs for Products
    path(
        'products/',
        viewsets.ProductList.as_view()
    ),
    path(
        'products/<slug:category_slug>/<slug:product_slug>/',
        viewsets.ProductDetail.as_view()
    ),

    # URLs for Categories
    path(
        'products/<slug:category_slug>/',
        viewsets.CategoryDetail.as_view()
    ),

]
