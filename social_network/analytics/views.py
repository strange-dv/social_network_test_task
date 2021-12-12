from datetime import datetime

from django.utils import timezone
from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from .utils import get_stats
from .serailizers import SocialNetworkUserAnalyticsSerializer


class PostAnalyticsView(APIView):
    DATETIME_FORMAT = "%Y-%m-%d"

    def get(self, request):
        today = timezone.now().date()

        from_date = request.GET.get("from_date", "")
        to_date = request.GET.get("to_date", "")

        if from_date:
            try:
                from_date = datetime.strptime(from_date, self.DATETIME_FORMAT).date()
            except ValueError:
                return Response(
                    {"details": "date format is not valid, use %Y-%m-%d format"}, 400
                )
        else:
            from_date = today

        if to_date:
            try:
                to_date = datetime.strptime(to_date, self.DATETIME_FORMAT).date()
            except ValueError:
                return Response(
                    {"details": "date format is not valid, use %Y-%m-%d format"}, 400
                )
        else:
            to_date = today

        return Response(get_stats(from_date, to_date))


class UserAnalyticsView(APIView):
    def get(self, _request, pk=None):
        if not pk:
            raise NotFound("user not found")

        instance = get_user_model().objects.get(id=pk)

        serializer = SocialNetworkUserAnalyticsSerializer(instance)
        return Response(serializer.data)
