from rest_framework.serializers import Serializer, ModelSerializer
from .models import CustomerUser
from django.contrib.auth.password_validation import validate_password as valid_password


class CustomerUserSerializer(ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = [
            'username',
            'email',
            'password'
        ]

    def validate_password(self, password):
        valid_password(password)
        return password

    def save(self):
        return CustomerUser.objects.create_user(**self.validated_data)
