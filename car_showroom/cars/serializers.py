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
        read_only_fields = ['id', 'car_type']
        extra_kwargs = {
            'year':{'required':True}
        }

    def validate_car_type(self, value):
        if value in dict(Car.CHOICES).keys():
            return value
        for key, val in Car.CHOICES:
            if val == value:
                return key
        raise serializers.ValidationError("Неверный тип автомобиля")

    def create(self, validated_data):
        car_type = validated_data.pop("get_car_type_display")
        validated_data['car_type'] = car_type
        return super().create(validated_data)
