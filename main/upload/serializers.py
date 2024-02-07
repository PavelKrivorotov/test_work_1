from rest_framework import serializers

from upload.models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = [
            'file',
            'uploaded_at',
            'processed'
        ]
        read_only_fields =[
            'uploaded_at',
            'processed'
        ]


class ListFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = [
            'file',
            'uploaded_at',
            'processed',
        ]

