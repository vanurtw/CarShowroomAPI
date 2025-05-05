from django.contrib import admin
from .models import Record, Service

# Register your models here.
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    pass



@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id']