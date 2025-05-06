from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser
from services.services import upload_photo_customer_user, validate_size_image
from django.core.validators import FileExtensionValidator





class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email обязателен')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)



class CustomerUser(AbstractUser):
    username = None
    email = models.EmailField("email address", unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Profile(models.Model):
    user = models.OneToOneField(
        'CustomerUser',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='user_profile'
    )
    first_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    avatar = models.ImageField(
        upload_to=upload_photo_customer_user,
        default='users/default.jpg',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg']), validate_size_image]

    )
    description = models.CharField(max_length=255, blank=True, null=True)
    date_birth = models.DateField(blank=True, null=True)
    points = models.IntegerField(default=0)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f'Профиль пользователя {self.user}'


    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
