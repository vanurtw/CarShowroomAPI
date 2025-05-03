from rest_framework import serializers
from .models import Record


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = [
            'id',
            'status',
            'car',
            'description',
            'recording_date',
            'date_create'
        ]
        read_only_fields = ['id', 'status', 'date_create']
