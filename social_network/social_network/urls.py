from django.contrib import admin
from django.urls import path, include

from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/auth/", include("accounts.urls")),
    path("api/v1/posts/", include("posts.urls")),
    path("api/v1/analytics/", include("analytics.urls")),
    path("api/v1/schema/", get_schema_view("SocialNetwork API Schema")),
    path("api/v1/docs/", include_docs_urls("SocialNetwork API Docs")),
]
