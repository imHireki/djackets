"""
URL settings for product app
"""

# Django
from django.urls import path

# Product app
from .views import (
    LatestProducts, ProductDetail,
    CategoryDetail, SearchProducts
)


urlpatterns = [
    path('search/', SearchProducts.as_view()),
    path('latest-products/', LatestProducts.as_view()),
    path('<slug:category_slug>/<slug:product_slug>/', ProductDetail.as_view()),
    path('<slug:category_slug>/', CategoryDetail.as_view()),
]
