"""
URL settings for product app
"""

# Django
from django.urls import path

# Django Rest Framework
from rest_framework.routers import DefaultRouter

# Product app
from .views import functions as func, generics as generics


urlpatterns = [

    # URLs for Functions
    path('Search/', func.SearchProducts.as_view()),
    path('AddToCart/', func.AddToCart.as_view()),
    path('DecreaseFromCart/', func.DecreaseOrDeleteFromCart.as_view()),
    path('DeleteFromCart/', func.DeleteFromCart.as_view()),

    # URLs for Cart
    path('cart/', generics.Cart.as_view()),

    # URLs for Products
    path('', generics.ProductList.as_view()),
    path('<slug:category_slug>/<slug:product_slug>/',
        generics.ProductDetail.as_view()),

    # URLs for Categories
    path('<slug:category_slug>/', generics.CategoryDetail.as_view()),
]
