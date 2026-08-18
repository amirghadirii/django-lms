from django.shortcuts import redirect
from django.conf import settings
from django.urls import reverse

class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path

        if getattr(settings, "MAINTENANCE_MODE", False):
            if path.startswith('/static/') or path.startswith('/media/') or path == reverse("maintenance"):
                return self.get_response(request)
            else:
                return redirect(reverse("maintenance"))

        return self.get_response(request)