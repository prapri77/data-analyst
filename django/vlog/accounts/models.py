from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from accounts.managers import customUsermanager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    full_name = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELD = []

    objects = customUsermanager()

    def __str__(self):
        return self.email
    




