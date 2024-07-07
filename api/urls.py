from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.contact_service.views import MenuItemViewSet

router = DefaultRouter()
router.register(r'menu-items', MenuItemViewSet, basename='menu-item')

urlpatterns = [
    path('contact/', include(router.urls)),
]
