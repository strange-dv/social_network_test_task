from django.urls import path

from . import views


urlpatterns = [
    path("", views.PostView.as_view()),
    path("<int:pk>/", views.PostDetailView.as_view()),
    path("like/<int:pk>/", views.LikePostView.as_view()),
    path("unlike/<int:pk>/", views.UnLikePostView.as_view()),
]
