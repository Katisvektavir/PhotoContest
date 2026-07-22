from models_app.timestamped.models import TimeStampedMixin
from models_app.user.models import CustomUser
from django.db import models


class Post(TimeStampedMixin):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="posts", null=True, blank=True)
    message = models.TextField(null=True, blank=True)