from django.db import models

class Like(models.Model):
    created_at = models.DateTimeField(auto_now=True)

