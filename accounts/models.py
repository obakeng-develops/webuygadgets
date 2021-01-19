from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomAccountManager

# Create your models here.
class Account(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), max_length=80, unique=True)
    username = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=10)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomAccountManager()

    def __str__(self):
        return self.email