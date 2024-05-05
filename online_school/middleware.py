from django.http import HttpResponseForbidden


class SecretAdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'secret-admin' in request.path and not request.user.is_staff:
            return HttpResponseForbidden("You do not have access to this page.")
        return self.get_response(request)
