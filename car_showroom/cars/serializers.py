from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.ModelSerializer):
    car_type = serializers.CharField(source='get_car_type_display')

    class Meta:
        model = Car
        fields = [
            'id',
            'car_type',
            'brand',
            'name',
            'year',
            'image'
        ]
