from io import BytesIO

from celery import shared_task

from minio_storage.client import client


@shared_task(bind=True)
def upload(self, file, filename, size, bucket_name):
    f = BytesIO(bytes.fromhex(file))

    client.put_object(
        bucket_name = bucket_name,
        object_name = filename,
        data = f,
        length = size
    )

    return {
        'result': 'success',
        'filename': filename,
    }


@shared_task(bind=True)
def tmp_upload(self, filepath, filename, bucket_name):
    client.fput_object(
        bucket_name  = bucket_name,
        object_name = filename,
        file_path = filepath
    )

    return {
        'result': 'success',
        'status': 'tmp-file',
        'filename': filename,
    }

