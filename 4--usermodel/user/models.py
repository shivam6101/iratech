from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

class user(models.Model):
    email=models.EmailField()
    phone=models.IntegerField()
    password=models.TextField()

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = user()