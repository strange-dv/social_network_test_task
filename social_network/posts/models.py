from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField()
    users_like = models.ManyToManyField(
        get_user_model(), related_name="posts_liked", blank=True
    )
    total_likes = models.PositiveIntegerField(db_index=True, default=0)

    def liked_by(self, user):
        return Post.objects.filter(id=self.id, users_like=user).exists()
