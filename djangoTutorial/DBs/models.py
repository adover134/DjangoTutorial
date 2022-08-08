from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)


class Car(models.Model):
    owner = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='owned')