from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    isLoggedIn = models.BooleanField(default=False)

class Task(models.Model):
    title = models.CharField(max_length=166)
    description = models.TextField()
    owner = models.TextField(default=timezone.now)
    isDone = models.BooleanField(default=False)