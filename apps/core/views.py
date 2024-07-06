import datetime
import logging
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework import status
from apps.contact_service.connector import ContactServiceConnector
from apps.contact_service.models import ContactService
from apps.core.models import History
from apps.core.serializers import HistorySerializer


logger = logging.getLogger(__name__)

# Create your views here.


class HistoryViewSet(ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer


class HistoryTwoViewSet(ViewSet):

    @action(detail=False, methods=['post'])
    def create_history(self, request, *args, **kwargs):
        user_id = self.request.data.get('user', None)
        description = self.request.data.get('description', None)
        history = History.objects.create(user_id, description=description)

        return Response(
            status=201,
            data={
                'id': history.id,
                'description': history.description,
                'trigger_date': history.trigger_date.strftime('y%-m%-d-%'),
            })


class ContactServiceViewSet(viewsets.ViewSet):
    def get_queryset(self):
        return ContactService.objects.all()

    def send_request(self, method, path, data=None):
        contact_service = self.get_queryset().last()
        if not contact_service:
            logger.error("No ContactService object found")
            return None

        full_endpoint = contact_service.endpoint
        contact_service_connector = ContactServiceConnector(endpoint=full_endpoint)
        return contact_service_connector.send_request(method, path, data=data)

    @action(detail=False, methods=['get'])
    def getAllBlogs(self, request, *args, **kwargs):
        logger.info(f"Request received: {request.method} {request.path}")
        response = self.send_request('get', 'api/blogs')
        if response:
            logger.info(f"Response status: {response.status_code}")
            return Response(data=response.json(), status=response.status_code)
        logger.error("Service not found")
        return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE,
                        data={'error': 'Service not found', 'request_path': request.path})

    @action(detail=False, methods=['post'])
    def create_blog(self, request, *args, **kwargs):
        logger.info(f"Request received: {request.method} {request.path}")
        response = self.send_request('post', 'api/blogs')
        if response:
            logger.info(f"Response status: {response.status_code}")
            return Response(data=response.json(), status=response.status_code)
        logger.error("Service not found")
        return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE,
                        data={'error': 'Service not found', 'request_path': request.path})

    @action(detail=True, methods=['get'])
    def get_blog_by_id(self, request, *args, **kwargs):
        blog_id = kwargs.get('pk')
        response = self.send_request('get', f'/{blog_id}')
        if response:
            return Response(data=response.json(), status=response.status_code)
        return Response(status=503, data={'service not found'})

    @action(detail=True, methods=['put'])
    def update_blog(self, request, *args, **kwargs):
        blog_id = kwargs.get('pk')
        response = self.send_request('put', f'/{blog_id}', data=request.data)
        if response:
            return Response(data=response.json(), status=response.status_code)
        return Response(status=503, data={'service not found'})

    @action(detail=True, methods=['delete'])
    def delete_blog(self, request, *args, **kwargs):
        blog_id = kwargs.get('pk')
        response = self.send_request('delete', f'/{blog_id}')
        if response:
            return Response(data=response.json(), status=response.status_code)
        return Response(status=503, data={'service not found'})

    @action(detail=False, methods=['get'])
    def get_authorization_url(self, request, *args, **kwargs):
        response = self.send_request('get', '/api/blogs')
        if response:
            return Response(data=response.json(), status=response.status_code)
        return Response(status=503, data={'service not found'})


class OutlookServiceViewSet(viewsets.ViewSet):
    def get_queryset(self):
        return ContactService.objects.all()

    def get_contact_connector(self):
        contact_service = self.get_queryset().last()
        if not contact_service:
            logger.error("No ContactService object found")
            return None
        return ContactServiceConnector(endpoint=contact_service.endpoint)

    @action(detail=False, methods=['get'])
    def get_authorization_url(self, request, *args, **kwargs):
        contact_connector = self.get_contact_connector()
        if not contact_connector:
            return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE, data={'error': 'Service not found'})

        response = contact_connector.get_authorization_url()
        if response:
            return Response(data=response.json(), status=response.status_code)
        return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE, data={'error': 'Service not found'})
