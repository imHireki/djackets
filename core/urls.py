from django.contrib import admin
from django.urls import path, include

"""
TODO: MAYBE IT'LL NEED :

Add rest_framework.authentication.TokenAuthentication
to Django REST Framework authentication strategies tuple:

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        (...)
    ),
 }
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
]
