from rest_framework.views import APIView
from rest_framework.response import Response
from apps.contact_service.views import MenuItemViewSet

class BaseProxyView(APIView):
    def dispatch(self, request, *args, **kwargs):
        view = self.get_view()
        return view(request, *args, **kwargs)

    def get_view(self):
        raise NotImplementedError("Subclasses must implement get_view()")
