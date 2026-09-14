from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    moderator = models.BooleanField(null=True, blank=True)

    class Meta:
        app_label = 'models_app'