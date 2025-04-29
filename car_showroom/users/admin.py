from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomerUser, Profile

@admin.register(CustomerUser)
class CustomerUserAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

