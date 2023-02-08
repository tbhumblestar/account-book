from django.db import models


class Url(models.Model):
    url = models.URLField()
    expired_at = models.DateTimeField()
