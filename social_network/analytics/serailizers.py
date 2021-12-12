from django.contrib.auth import get_user_model

from rest_framework import serializers


class SocialNetworkUserAnalyticsSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ["id", "last_login", "last_seen"]
