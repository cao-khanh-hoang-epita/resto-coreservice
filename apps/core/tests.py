from django.test import TestCase
from unittest.mock import patch
from rest_framework.test import APIClient
from .views import BaseProxyView

class BaseProxyViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    @patch('apps.core.views.requests.request')
    def test_proxy_request(self, mock_request):
        mock_request.return_value.json.return_value = {'data': 'test'}
        mock_request.return_value.status_code = 200

        view = BaseProxyView()
        response = view.get(request=self.client.get('/test/'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'data': 'test'})

    # Add more tests as needed
