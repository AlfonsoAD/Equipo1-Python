from django.db import models
from django.utils import timezone


class Animal(models.Model):
    name = models.CharField(max_length=255)
    race = models.CharField(max_length=255)
    admission_date = models.DateTimeField(default=timezone.now)
    departure_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.name}-{self.race}"


class AnimalDetail(models.Model):
    weight = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=True)
    animal = models.OneToOneField(
        Animal, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return F"{self.weight} - {self.color}"
