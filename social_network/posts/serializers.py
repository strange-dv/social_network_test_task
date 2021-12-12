from rest_framework import serializers

from . import models


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "content", "creator", "total_likes")
        read_only_fields = ["total_likes", "creator"]
        model = models.Post

    def create(self, validated_data):
        return models.Post.objects.create(
            content=validated_data["content"],
            creator=self.context["request"].user
        )
