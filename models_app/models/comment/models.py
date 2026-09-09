from models_app.models.post.models import Post
from models_app.models.timestamped.models import TimeStampedMixin
from models_app.models.user.models import CustomUser
from django.db import models


class Comment(TimeStampedMixin):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="comments", null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", null=True, blank=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True)
