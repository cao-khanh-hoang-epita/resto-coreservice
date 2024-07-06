from django.urls import path, re_path
from .views import MenuItemViewSet

urlpatterns = [
    re_path(r'^menu-items/?$', MenuItemViewSet.as_view({'get': 'list', 'post': 'create'})),
    re_path(r'^menu-items/(?P<pk>[0-9]+)/?$', MenuItemViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
]
