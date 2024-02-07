import os

from minio.api import Minio


client = Minio(
    endpoint = f"{os.getenv('MINIO_HOST')}:{os.getenv('MINIO_PORT')}",
    access_key = os.getenv('MINIO_ACCESS_KEY'),
    secret_key = os.getenv('MINIO_SECRET_KEY'),
    secure = False,
)

