from django.core.validators import MinValueValidator
from django.db import models
from users.models import Profile
from services.services import upload_photo_car




class Car(models.Model):
    CHOICES = [
        ('S', 'sedan'),
        ('M', 'minivan'),
        ('H', 'hatchback')
    ]

    profile_user = models.ForeignKey(
        Profile,
        related_name='profile_cars',
        on_delete=models.CASCADE
    )
    car_type = models.CharField(
        max_length=1,
        blank=True,
        null=True,
        choices=CHOICES
    )
    brand = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1900)])
    image = models.ImageField(
        upload_to=upload_photo_car,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'Машина {self.name} пользователя {self.profile_user.user}'


    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'