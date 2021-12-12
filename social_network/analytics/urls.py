from django.urls import path

from . import views


urlpatterns = [
    path("", views.PostAnalyticsView.as_view()),
    path("users/<int:pk>/", views.UserAnalyticsView.as_view()),
]
