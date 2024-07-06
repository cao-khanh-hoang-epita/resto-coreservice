import requests
from django.http import JsonResponse, HttpResponse
from django.views import View
import logging

logger = logging.getLogger(__name__)

class ProxyView(View):
    def get(self, request, path, *args, **kwargs):
        url = f"http://localhost:3001/api/{path}"
        logger.debug(f"Proxying GET request to URL: {url} with params: {request.GET} and headers: {self.get_headers(request)}")
        response = requests.get(url, params=request.GET, headers=self.get_headers(request))
        return self.create_response(response)

    def post(self, request, path, *args, **kwargs):
        url = f"http://localhost:3001/api/{path}"
        logger.debug(f"Proxying POST request to URL: {url} with data: {request.body} and headers: {self.get_headers(request)}")
        response = requests.post(url, data=request.body, headers=self.get_headers(request))
        return self.create_response(response)

    def put(self, request, path, *args, **kwargs):
        url = f"http://localhost:3001/api/{path}"
        logger.debug(f"Proxying PUT request to URL: {url} with data: {request.body} and headers: {self.get_headers(request)}")
        response = requests.put(url, data=request.body, headers=self.get_headers(request))
        return self.create_response(response)

    def delete(self, request, path, *args, **kwargs):
        url = f"http://localhost:3001/api/{path}"
        logger.debug(f"Proxying DELETE request to URL: {url} with headers: {self.get_headers(request)}")
        response = requests.delete(url, headers=self.get_headers(request))
        return self.create_response(response)

    def get_headers(self, request):
        headers = {key: value for key, value in request.headers.items() if key != 'Host'}
        return headers

    def create_response(self, response):
        return HttpResponse(response.content, status=response.status_code, content_type=response.headers.get('Content-Type'))
