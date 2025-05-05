from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomerUser, Profile

@admin.register(CustomerUser)
class CustomerUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'is_staff']
    list_display_links = ['id', 'username']
    list_filter = ['is_staff']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

