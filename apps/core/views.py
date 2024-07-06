from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ApiLog
from .serializers import ApiLogSerializer

class HealthCheckView(APIView):
    def get(self, request):
        return Response({"status": "healthy"}, status=status.HTTP_200_OK)

class ApiLogView(APIView):
    def get(self, request):
        logs = ApiLog.objects.all()[:100]  # Get the last 100 logs
        serializer = ApiLogSerializer(logs, many=True)
        return Response(serializer.data)
