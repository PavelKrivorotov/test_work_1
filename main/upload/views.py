from rest_framework.permissions import AllowAny
from rest_framework import generics

from upload.models import File
from upload import serializers

# Initialize celery signals
from upload import signals


class UploadFileView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.FileSerializer


class ListFileView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.ListFileSerializer
    queryset = File.objects.all()

