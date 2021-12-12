from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class SocialNetworkUser(AbstractUser):
    last_seen = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username
