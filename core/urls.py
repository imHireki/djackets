"""
URL configuration
"""

# Django
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

# Django Rest Framework
from rest_framework.routers import DefaultRouter

# Apps
from apps.product import viewsets


urlpatterns = [
    path('admin/', admin.site.urls),

    # Product
    path('api/v2/', include('apps.product.urls')),

    # Djoser
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
]

# Media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
