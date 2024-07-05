# api/middleware.py

import requests

class ReverseProxyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request path starts with '/api/'
        if request.path.startswith('/api/'):
            url = f'http://localhost:3001{request.path}'
            # Forward the request to the CRUD service
            response = requests.request(
                method=request.method,
                url=url,
                headers=request.headers,
                data=request.body,
                params=request.GET
            )
            # Return the response from the CRUD service
            return response

        return self.get_response(request)
