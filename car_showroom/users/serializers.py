from rest_framework import serializers

from cars.serializers import CarSerializer
from .models import CustomerUser, Profile
from django.contrib.auth.password_validation import validate_password as valid_password


class CustomerUserSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=15)

    class Meta:
        model = CustomerUser
        fields = [
            'email',
            'phone',
            'password',
        ]

    def validate_password(self, password):
        valid_password(password)
        return password

    def save(self):
        user = CustomerUser.objects.create_user(**self.validated_data)
        Profile.objects.create(user=user, first_name=user.email)
        return user


class CustomerUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = ['phone', 'email']


class CustomerUserProfileSerializer(serializers.ModelSerializer):
    cars = CarSerializer(source="profile_cars", many=True)
    user = CustomerUserDetailSerializer()

    class Meta:
        model = Profile
        fields = [
            'id',
            'user',
            'first_name',
            'last_name',
            'avatar',
            'description',
            'date_birth',
            'points',
            'cars'
        ]


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id',
            'first_name',
            'last_name',
            'avatar',
            'description',
            'date_birth',
            'points',
        ]
        extra_kwargs = {
            'points': {'read_only': True},
            'id': {'read_only': True},
        }
