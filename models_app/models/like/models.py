from models_app.models.post.models import Post
from models_app.models.comment.models import Comment
from models_app.models.timestamped.models import TimeStampedMixin
from models_app.models.user.models import CustomUser
from django.db import models
from django.db.models import Q


class Like(TimeStampedMixin):
    created_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True
    )

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="likes",
        related_query_name="like",
        null=False,
        blank=False
    )

    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name="likes",
        related_query_name="like",
        null=True,
        blank=True
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="likes",
        related_query_name="like",
        null=True,
        blank=True
    )

    def __str__(self):
        return str(self.user) + str(self.post)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=(
                        Q(post__isnull=False, comment__isnull=True)
                        | Q(post__isnull=True, comment__isnull=False)
                ),
                name="like_exactly_one_target",
            ),
            models.UniqueConstraint(
                fields=["user", "post"],
                name="unique_user_post_like",
            ),
            models.UniqueConstraint(
                fields=["user", "comment"],
                name="unique_user_comment_like",
            ),
        ]

