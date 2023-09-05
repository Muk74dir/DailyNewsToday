from django.db import models
from django.contrib.auth.models import User
from .constants import *

class UserRegistrationModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE)
    gender = models.CharField(max_length=10, choices=GENDER_TYPE)
    birth_date = models.DateField()
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


