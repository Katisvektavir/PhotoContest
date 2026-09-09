from models_app.models.post.models import Post
from models_app.models.timestamped.models import TimeStampedMixin
from models_app.models.user.models import CustomUser
from django.db import models


class Photo(TimeStampedMixin):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="photos", null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="photos", null=True, blank=True)
    name = models.CharField(max_length=64, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
