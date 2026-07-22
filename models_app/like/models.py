from models_app.post.models import Post
from models_app.comment.models import Comment
from models_app.timestamped.models import TimeStampedMixin
from models_app.user.models import CustomUser
from django.db import models


class Like(TimeStampedMixin):
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="likes", null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="likes", null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes", null=True, blank=True)

