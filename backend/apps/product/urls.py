from django.urls import include, path
from . import views


urlpatterns = [
    path('latest-products', views.LatestProductList.as_view()),
]

