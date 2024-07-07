import requests
from django.conf import settings
from django.http import JsonResponse

class ProxyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Proxy requests to menu service
        if request.path.startswith('/api/menu/'):
            menu_url = f"{settings.MENU_SERVICE_URL}{request.path.replace('/api/menu/', '/')}?{request.META['QUERY_STRING']}"
            menu_response = requests.request(
                method=request.method,
                url=menu_url,
                headers={key: value for key, value in request.headers.items() if key != 'Host'},
                data=request.body,
                cookies=request.COOKIES,
                allow_redirects=False,
            )
            return JsonResponse(menu_response.json(), status=menu_response.status_code)

        # Proxy requests to cart service
        elif request.path.startswith('/api/cart/'):
            cart_url = f"{settings.CART_SERVICE_URL}{request.path.replace('/api/cart/', '/')}?{request.META['QUERY_STRING']}"
            cart_response = requests.request(
                method=request.method,
                url=cart_url,
                headers={key: value for key, value in request.headers.items() if key != 'Host'},
                data=request.body,
                cookies=request.COOKIES,
                allow_redirects=False,
            )
            return JsonResponse(cart_response.json(), status=cart_response.status_code)

        return response
