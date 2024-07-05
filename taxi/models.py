from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name} {self.country}"

    class Meta:
        ordering = ["name"]


class Driver(AbstractUser):
    license_number = models.CharField(max_length=100, unique=True)


class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer,
                                     on_delete=models.CASCADE,
                                     related_name="cars")
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                     related_name="cars")

    def __str__(self) -> str:
        return f"{self.model} {self.manufacturer.name}"

    class Meta:
        ordering = ["model"]