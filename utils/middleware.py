# myapp/middleware.py
from django.shortcuts import redirect
from django.conf import settings


class PhoneVerificationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and not request.user.phone_number_verified:
            if request.path not in ['/accounts/update-phone-number/', 'accounts/logout/', '/accounts/verify-phone/']:
                return redirect(settings.SSO_URL+'/verify-phone/')
        response = self.get_response(request)
        return response
