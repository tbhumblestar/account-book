from django.db import models
from django.utils import timezone


class Url(models.Model):
    url = models.URLField()
    expired_at = models.DateTimeField(
        default=timezone.now() + timezone.timedelta(days=3),
    )
