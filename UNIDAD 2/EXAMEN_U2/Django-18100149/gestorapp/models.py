from django.utils import timezone
from django.db import models
from webapp.models import Animal

# Create your models here.


class Doctor(models.Model):
    fullname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50)
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.fullname


class Clinic(models.Model):
    name = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=True)
    doctor = models.ForeignKey(
        Doctor, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Consultation(models.Model):
    service = models.CharField(max_length=255)
    price = models.FloatField()
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=True)
    doctor = models.ForeignKey(
        Doctor, on_delete=models.SET_NULL, null=True)
    animal = models.OneToOneField(Animal, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f" Service: {self.service}, Dr: {self.doctor.fullname}, Animal: {self.animal.name}"
