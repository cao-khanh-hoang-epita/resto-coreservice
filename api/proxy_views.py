from .proxy_view import BaseProxyView

class MenuProxyView(BaseProxyView):
    def proxy_request(self, request, path=''):
        return super().proxy_request(request, f"menu-items/{path}")
