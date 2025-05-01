from django.contrib import admin
from .models import Car, Record


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    pass
