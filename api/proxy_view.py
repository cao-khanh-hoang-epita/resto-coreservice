from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from django.conf import settings

class BaseProxyView(APIView):
    service_url = settings.CRUD_SERVICE_URL

    def proxy_request(self, request, path=''):
        method = request.method.lower()
        url = f"{self.service_url}/{path}"
        headers = {'Content-Type': 'application/json'}
        data = request.data if method in ['post', 'put', 'patch'] else None
        params = request.query_params if method == 'get' else None

        try:
            response = requests.request(method, url, json=data, params=params, headers=headers)
            return Response(response.json(), status=response.status_code)
        except requests.RequestException as e:
            return Response({'error': str(e)}, status=500)
