from django.contrib import admin
from .models import UserRegistrationModel

@admin.register(UserRegistrationModel)
class UserRegistrationAdmin(admin.ModelAdmin):
    list_display = ['user', 'account_type']

    def __self__(self, obj):
        return obj.user.username
