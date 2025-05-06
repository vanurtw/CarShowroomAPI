from django.db import models
from users.models import Profile
from cars.models import Car


# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    price = models.IntegerField()
    active = models.BooleanField(default=True)
    date_create = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


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
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    service = models.ForeignKey(
        'Service',
        on_delete=models.CASCADE,
        related_name='service_records'
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
    recording_date = models.DateTimeField()
    description = models.CharField(max_length=500, blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Заказ пользователя {self.profile.user} на машину {self.car.name}'


    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
