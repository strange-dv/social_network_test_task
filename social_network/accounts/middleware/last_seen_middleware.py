from django.contrib.auth.models import AnonymousUser
from django.utils import timezone


class UpdateLastSeenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user

        if not isinstance(user, AnonymousUser):
            user.last_seen = timezone.now()
            user.save()

        response = self.get_response(request)

        return response
