from .proxy_view import BaseProxyView
from apps.contact_service.views import MenuItemViewSet

class MenuProxyView(BaseProxyView):
    def get_view(self):
        return MenuItemViewSet.as_view({'get': 'list', 'post': 'create'})
