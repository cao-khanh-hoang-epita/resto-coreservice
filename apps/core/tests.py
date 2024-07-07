from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import APILog

class HealthCheckTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_health_check(self):
        url = reverse('health_check')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"status": "healthy"})

class APILogTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        APILog.objects.create(method='GET', path='/api/test', status_code=200)

    def test_api_log_list(self):
        url = reverse('api_log_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
