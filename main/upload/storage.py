from secrets import token_urlsafe

from django.core.files.storage import Storage

from minio_storage.client import client


class MinioStorage(Storage):
    bucket_name = 'upload-bucket'

    def _open(self, name, mode='rb'):
        pass

    def _save(self, name, content):
        if not client.bucket_exists(self.bucket_name):
            client.make_bucket(self.bucket_name)

        # 
        # Add to celary task!
        # 
        client.put_object(
            bucket_name = self.bucket_name,
            object_name = name,
            data = content,
            length=content.size
        )
        # 
        # 

        return name
    
    def get_available_name(self, name, max_length=None):
        filename =  super().get_available_name(name, max_length)
        name, ext = filename.split('.')
        return f'{name}_{token_urlsafe(5)}.{ext}'
    
    def exists(self, name: str) -> bool:
        return False
    
    def url(self, name):
       return client.get_presigned_url(
           method = 'GET',
           bucket_name = self.bucket_name,
           object_name = name
        )

