from models_app.models.post.models import Post
from models_app.models.timestamped.models import TimeStampedMixin
from models_app.models.user.models import CustomUser
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.db import models



def photo_directory_path(instance, filename):
    if instance.is_avatar:
        return f"user_{instance.user_id}/avatars/{filename}"
    elif instance.post_id:
        return f"posts/{filename}"
    else:
        return f"user_{instance.user_id}/{filename}"


class Photo(TimeStampedMixin):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="photos",
        related_query_name="photo",
        null=False,
        blank=False
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="photos",
        related_query_name="photo",
        null=True,
        blank=True
    )

    name = models.CharField(
        max_length=64,
        null=True,
        blank=True
    )

    image = models.ImageField(
        null=True,
        blank=True,
        upload_to=photo_directory_path,
    )

    is_avatar = models.BooleanField()
    def __str__(self):
        return str(self.name)

    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(300, 300)],
        format='JPEG',
        options={'quality': 80}
    )