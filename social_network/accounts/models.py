from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

from analytics.utils import update_stats


class SocialNetworkUser(AbstractUser):
    last_seen = models.DateTimeField(default=timezone.now)

    def like(self, post):
        if not post.liked_by(self):
            post.users_like.add(self)
            post.total_likes += 1
            post.save()

            update_stats()

    def unlike(self, post):
        if post.liked_by(self):
            post.users_like.remove(self)
            post.total_likes -= 1
            post.save()

            update_stats(decrease=True)

    def __str__(self):
        return self.username
