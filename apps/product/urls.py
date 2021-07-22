"""
URL settings for product app
"""

# Django
from django.urls import path, include
from rest_framework import urlpatterns

# Django Rest Framework
from rest_framework.routers import DefaultRouter

# Product app
from . import viewsets

r = DefaultRouter()
r.register(r'products', viewsets.ProductList)

urlpatterns = r.urls

urlpatterns += [
    # path('products/', viewsets.ProductList.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/',
    viewsets.ProductDetail.as_view()),
    path('products/<slug:category_slug>/', viewsets.CategoryDetail.as_view()),
]
