from django.urls import path
from . import views


urlpatterns = [
    path('checkout/', views.checkout),
    path('orders/', views.OrderList.as_view())
]