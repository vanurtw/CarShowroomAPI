from django.db import models
from users.models import Profile
from cars.models import Car


# Create your models here.


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
    recording_date = models.DateField()
    description = models.CharField(max_length=500, blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Заказ пользователя {self.profile.user} на машину {self.car.name}'
