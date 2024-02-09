import os
from secrets import token_urlsafe

from django.conf import settings
from django.core.files.storage import Storage

from minio_storage.client import client
from upload.tasks import upload, tmp_upload


class MinioStorage(Storage):
    bucket_name = 'upload-bucket'

    def _open(self, name, mode='rb'):
        pass

    def _save(self, name, content):
        if not client.bucket_exists(self.bucket_name):
            client.make_bucket(self.bucket_name)

        if content.size < settings.FILE_UPLOAD_MAX_MEMORY_SIZE:
            c = content.file.read().hex()
            upload.apply_async(args=[c, name, content.size, self.bucket_name])

        else:
            tmp_upload.apply_async(args=[content.file.name, name, self.bucket_name])

        return name
    
    def get_available_name(self, name, max_length=None):
        filename =  super().get_available_name(name, max_length)
        name, ext = filename.split('.')
        return f'{name}_{token_urlsafe(5)}.{ext}'
    
    def exists(self, name: str) -> bool:
        return False
    
    def url(self, name: str):
       _url = client.get_presigned_url(
           method = 'GET',
           bucket_name = self.bucket_name,
           object_name = name
        )
       
       return self._url_extend(_url)

    def _url_extend(self, url: str):
        extend = os.getenv('MINIO_EXTEND')
        
        if extend.upper() == 'TRUE':
            old = '{}:{}'.format(
                os.getenv('MINIO_HOST'),
                os.getenv('MINIO_PORT')
            )
            new = '{}:{}'.format(
                os.getenv('MINIO_EXTEND_HOST'),
                os.getenv('MINIO_EXTEND_PORT')
            )
            url = url.replace(old, new)
        
        return url

