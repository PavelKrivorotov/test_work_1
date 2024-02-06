from django.db import models
from django.utils.timezone import now


class File(models.Model):
    file = models.FileField()
    uploaded_at = models.DateTimeField(default=now)
    processed = models.BooleanField(default=False)

