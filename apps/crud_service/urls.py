# crud_service/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.proxy_blog_list, name='blog-list-proxy'),
    # Add more paths for other CRUD operations as needed
]
