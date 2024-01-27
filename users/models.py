from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(null=True, max_length=150, blank=True)
    last_name = models.CharField(null=True, max_length=150, blank=True)
