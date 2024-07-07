from django.test import TestCase
from rest_framework.test import APIClient
from unittest.mock import patch
from .views import MenuItemViewSet

class MenuItemViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    @patch('apps.core.views.requests.request')
    def test_list_menu_items(self, mock_request):
        mock_request.return_value.json.return_value = [{'id': 1, 'name': 'Test Item'}]
        mock_request.return_value.status_code = 200

        response = self.client.get('/contact/menu-items/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [{'id': 1, 'name': 'Test Item'}])

    # Add more tests for create, retrieve, update, and destroy methods
