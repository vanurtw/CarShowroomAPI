from rest_framework import serializers
from .models import CustomerUser, Profile
from django.contrib.auth.password_validation import validate_password as valid_password


class CustomerUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    class Meta:
        model = CustomerUser
        fields = [
            'username',
            'email',
            'password',
        ]

    def validate_password(self, password):
        valid_password(password)
        return password

    def save(self):
        user =  CustomerUser.objects.create_user(**self.validated_data)
        Profile.objects.create(user=user, first_name=user.username)
        return user