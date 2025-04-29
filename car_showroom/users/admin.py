from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomerUser

@admin.register(CustomerUser)
class CustomerUserAdmin(admin.ModelAdmin):
    pass


