from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin #default django user admin

from core import models

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email','name']


admin.site.register(models.User, UserAdmin)
