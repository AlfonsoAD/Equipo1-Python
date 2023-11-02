from django.db import models
from django.utils import timezone
from directors.models import Technical_Director
from leagues.models import League


class Team(models.Model):
    name = models.CharField(max_length=255)
    league = models.CharField(max_length=255)
    count_players = models.IntegerField()
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(blank=True, null=True)
    # Un equipo tiene un director técnico y viceversa
    technical_director = models.OneToOneField(
        Technical_Director, on_delete=models.SET_NULL, null=True)
    # Un equipo pertenece a una liga y una liga tiene muchos equipos
    league = models.ForeignKey(League, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"{self.name}"
