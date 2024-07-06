from django.contrib import admin
from django.urls import path, include
from .home import home_view
from .proxy_views import MenuProxyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('api/menu/', MenuProxyView.as_view(), name='menu_proxy'),
    path('core/', include('apps.core.urls')),
    path('contact/', include('apps.contact_service.urls')),
]
