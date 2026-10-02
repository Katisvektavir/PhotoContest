from models_app.models.timestamped.models import TimeStampedMixin
from models_app.models.user.models import CustomUser
from django.db import models


class Post(TimeStampedMixin):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="posts",
        related_query_name="photo",
        null=True,
        blank=False
    )

    message = models.TextField(
        null=True,
        blank=True
    )