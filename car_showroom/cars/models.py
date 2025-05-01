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
    year = models.DateField(blank=True, null=True)
    image = models.ImageField(
        upload_to=upload_photo_car,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'Машина {self.name} пользователя {self.profile_user.user}'


class Record(models.Model):
    CHOICES = [
        ('P', 'pending'),
        ('A', 'approved'),
        ('R', 'rejected'),
        ('C', 'completed')
    ]

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='profile_records'
    )
    status = models.CharField(
        max_length=1,
        choices=CHOICES,
        default='P'
    )
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name='car_records'
    )
    description = models.CharField(max_length=500, blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Заказ пользователя {self.profile.user} на машину {self.car.name}'
