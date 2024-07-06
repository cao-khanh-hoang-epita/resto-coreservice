from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import ApiLog

class HealthCheckTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_health_check(self):
        response = self.client.get('/api/health/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"status": "healthy"})

class ApiLogTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        ApiLog.objects.create(method='GET', path='/api/test/', status_code=200, duration=0.1)

    def test_api_log_list(self):
        response = self.client.get('/api/logs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
