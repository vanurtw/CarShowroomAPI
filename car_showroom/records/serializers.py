from rest_framework import serializers
from .models import Record, Service
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            'id',
            'name',
            'description',
            'price',
            'active',
            'date_create'
        ]


class RecordSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)

    class Meta:
        model = Record
        fields = [
            'id',
            'status',
            'car',
            'service',
            'description',
            'recording_date',
            'date_create'
        ]
        read_only_fields = ['id', 'status', 'date_create']

    def validate_car(self, car):
        profile = self.context.get('profile')
        profile_cars = profile.profile_cars.all()
        if car in profile_cars:
            return car
        raise ValidationError("This is not your car")


