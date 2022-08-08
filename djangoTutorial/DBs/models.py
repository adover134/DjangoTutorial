from django.db import models
from django.contrib.auth.models import AbstractUser


class Person(models.Model):
    name = models.CharField(max_length=20)


class Car(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=10)
    owner = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='owned')


class User(AbstractUser):
    birth_day = models.DateField(null=True, default=None)
