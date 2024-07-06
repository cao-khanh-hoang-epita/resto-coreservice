from django.urls import path
from .views import HealthCheckView, ApiLogView

urlpatterns = [
    path('health/', HealthCheckView.as_view(), name='health_check'),
    path('logs/', ApiLogView.as_view(), name='api_logs'),
]
