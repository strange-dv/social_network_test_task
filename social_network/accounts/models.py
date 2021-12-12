from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class SocialNetworkUser(AbstractUser):
    last_seen = models.DateTimeField(default=timezone.now)

    def like(self, post):
        if not post.liked_by(self):
            post.users_like.add(self)
            post.total_likes += 1
            post.save()

    def unlike(self, post):
        if post.liked_by(self):
            post.users_like.remove(self)
            post.total_likes -= 1
            post.save()

    def __str__(self):
        return self.username
