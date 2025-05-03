from rest_framework import serializers
from .models import Record
from rest_framework.exceptions import ValidationError


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

    def validate_car(self, car):
        profile_cars = self.instance.profile.profile_cars.all()
        if car in profile_cars:
            return car
        raise ValidationError("This is not your car")
