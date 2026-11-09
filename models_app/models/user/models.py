from django.db import models
from django.templatetags.static import static
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    moderator = models.BooleanField(
        null=True,
        blank=True
    )

    avatar = models.OneToOneField(
        'Photo',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='user_avatar'
    )
    @property
    def avatar_url(self):
        # Если аватарка есть и у неё есть файл — отдаем её URL
        if self.avatar and self.avatar.image:
            return self.avatar.image.url
        # Если нет — отдаем статичную заглушку
        return static('img/default_avatar.png')

    class Meta:
        app_label = 'models_app'