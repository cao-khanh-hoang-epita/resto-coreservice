import time
from apps.core.models import ApiLog

class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        
        response = self.get_response(request)
        
        duration = time.time() - start_time
        
        ApiLog.objects.create(
            method=request.method,
            path=request.path,
            status_code=response.status_code,
            duration=duration
        )
        
        return response