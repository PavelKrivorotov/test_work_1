from django.db import models
from django.utils.timezone import now

from upload.storage import MinioStorage


class File(models.Model):
    # Set index on field `file` because make search on this field
    # for update `processed = True` after put file in Minio.
    # (Then celery task successed)
    file = models.FileField(
        storage = MinioStorage,
        db_index=True,
    )
    uploaded_at = models.DateTimeField(
        default = now,
    )
    processed = models.BooleanField(
        default = False,
    )

