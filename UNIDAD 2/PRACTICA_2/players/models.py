from django.db import models
from django.utils import timezone
from teams.models import Team


class Player(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    position = models.CharField(max_length=255)
    shirt_number = models.IntegerField()
    country = models.CharField(max_length=255)
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(blank=True, null=True)
    # Un jugador pertenece a un equipo y un equipo tiene muchos jugadores
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
