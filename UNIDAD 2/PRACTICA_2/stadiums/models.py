from django.db import models
from django.utils import timezone
from teams.models import Team


class Stadium(models.Model):
    name = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    capacity = models.IntegerField()
    country = models.CharField(max_length=255)
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(blank=True, null=True)
    team = models.OneToOneField(Team, on_delete=models.SET_NULL, null=True)
    # Un estadio pertenece a un equipo y un equipo tiene un estadio

    def __str__(self) -> str:
        return f"{self.name} {self.capacity}"
