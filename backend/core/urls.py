from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('apps.product.urls')),
    path('api/v1/', include('apps.order.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

