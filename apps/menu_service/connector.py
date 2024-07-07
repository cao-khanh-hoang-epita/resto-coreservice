# apps/core/connector.py
import requests

MENU_SERVICE_URL = 'http://resto-menuservice:8001/api/menu/'

def fetch_menu_items():
    try:
        response = requests.get(MENU_SERVICE_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching menu items: {e}")
        return None
