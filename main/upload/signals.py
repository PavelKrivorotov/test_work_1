from celery.signals import task_success

from upload.models import File


@task_success.connect
def upload_success(sender=None, headers=None, body=None, **kwargs):
    filename = kwargs.get('result')['filename']

    # Cghange File.processed attr on True:
    obj = File.objects.get(file=filename)
    obj.processed = True
    obj.save()

