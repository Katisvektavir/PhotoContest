from django.db import models

class TimeStampedMixin(models.Model):
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True