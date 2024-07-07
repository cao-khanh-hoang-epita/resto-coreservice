from rest_framework import viewsets
from rest_framework.response import Response
from api.proxy_view import BaseProxyView

class MenuItemViewSet(BaseProxyView, viewsets.ViewSet):
    def list(self, request):
        return self.proxy_request(request, 'menu-items/')

    def create(self, request):
        return self.proxy_request(request, 'menu-items/')

    def retrieve(self, request, pk=None):
        return self.proxy_request(request, f'menu-items/{pk}/')

    def update(self, request, pk=None):
        return self.proxy_request(request, f'menu-items/{pk}/')

    def destroy(self, request, pk=None):
        return self.proxy_request(request, f'menu-items/{pk}/')
