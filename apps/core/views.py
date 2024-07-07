import requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ProxyView(APIView):
    service_url = None

    def proxy_request(self, request, *args, **kwargs):
        method = request.method.lower()
        url = f"{self.service_url}{request.path}"
        data = request.data if method in ['post', 'put', 'patch'] else None
        try:
            response = requests.request(method, url, json=data, params=request.query_params)
            return Response(response.json(), status=response.status_code)
        except requests.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

    def get(self, request, *args, **kwargs):
        return self.proxy_request(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.proxy_request(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.proxy_request(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.proxy_request(request, *args, **kwargs)

class MenuProxyView(ProxyView):
    service_url = settings.MENU_SERVICE_URL

class CartProxyView(ProxyView):
    service_url = settings.CART_SERVICE_URL
