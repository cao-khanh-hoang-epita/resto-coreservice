# apps/core/connector.py
import requests

CART_SERVICE_URL = 'http://resto-cartservice:8002/api/cart/'

def fetch_cart_items():
    try:
        response = requests.get(CART_SERVICE_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching cart items: {e}")
        return None
