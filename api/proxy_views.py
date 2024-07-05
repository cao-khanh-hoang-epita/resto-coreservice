# proxy_views.py

import requests
from django.http import HttpResponse
from django.views import View

class ProxyView(View):
    def get(self, request, path, *args, **kwargs):
        url = f"http://localhost:3001/api/{path}"
        response = requests.get(url, params=request.GET, headers=request.headers)
        return HttpResponse(response.content, status=response.status_code, content_type=response.headers.get('Content-Type', 'application/json'))

    def post(self, request, path, *args, **kwargs):
        url = f"http://localhost:3001/api/{path}"
        response = requests.post(url, data=request.body, headers=request.headers)
        return HttpResponse(response.content, status=response.status_code, content_type=response.headers.get('Content-Type', 'application/json'))

    def put(self, request, path, *args, **kwargs):
        url = f"http://localhost:3001/api/{path}"
        response = requests.put(url, data=request.body, headers=request.headers)
        return HttpResponse(response.content, status=response.status_code, content_type=response.headers.get('Content-Type', 'application/json'))

    def delete(self, request, path, *args, **kwargs):
        url = f"http://localhost:3001/api/{path}"
        response = requests.delete(url, headers=request.headers)
        return HttpResponse(response.content, status=response.status_code, content_type=response.headers.get('Content-Type', 'application/json'))
