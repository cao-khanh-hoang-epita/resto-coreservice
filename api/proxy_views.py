import requests
from django.http import JsonResponse
from django.conf import settings

def proxy_menu_request(request):
    menu_url = f"http://{settings.MENU_SERVICE_URL}/api/menu/{request.path_info.replace('/api/menu/', '')}"
    response = requests.get(menu_url)
    return JsonResponse(response.json(), status=response.status_code)

def proxy_cart_request(request):
    cart_url = f"http://{settings.CART_SERVICE_URL}/api/cart/{request.path_info.replace('/api/cart/', '')}"
    response = requests.get(cart_url)
    return JsonResponse(response.json(), status=response.status_code)
