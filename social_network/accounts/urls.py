from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    path("refresh/", TokenRefreshView.as_view()),
    path("registration/", include("dj_rest_auth.registration.urls")),
]
