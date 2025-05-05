from django.contrib import admin
from .models import Record, Service

# Register your models here.
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'service', 'profile', 'status']
    list_filter = ['profile', 'service', 'status']



@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'active']
    list_display_links = ['id', 'name']
    list_filter = ['active']