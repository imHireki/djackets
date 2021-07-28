"""
URL settings for project's root

The `urlpatterns` list routes URLs to views
"""

# Django
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

# Apps
from apps.product import views


urlpatterns = [
    path('admin/', admin.site.urls),

    # Project apps
    path('api/v1/products/', include('apps.product.urls')),

    # Djoser users and auth
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),

]

# Media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
