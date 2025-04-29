from django.db import models
from django.contrib.auth.models import AbstractUser
from services.services import upload_photo_customer_user, validate_size_image
from django.core.validators import FileExtensionValidator


class CustomerUser(AbstractUser):
    avatar = models.ImageField(
        upload_to=upload_photo_customer_user,
        default='users/default.jpg',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg']), validate_size_image]

    )
