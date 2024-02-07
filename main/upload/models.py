from django.db import models
from django.utils.timezone import now

from upload.storage import MinioStorage


class File(models.Model):
    # file = models.FileField()

    file = models.FileField(
        storage = MinioStorage
    )
    uploaded_at = models.DateTimeField(
        default = now
    )
    processed = models.BooleanField(
        default = False
    )

