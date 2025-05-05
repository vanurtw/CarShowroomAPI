from django.contrib import admin
from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'name', 'car_type', 'profile_user']
    list_display_links = ['id', 'brand']
    list_filter = ['car_type', 'profile_user']
    search_fields = ['brand', 'name']



