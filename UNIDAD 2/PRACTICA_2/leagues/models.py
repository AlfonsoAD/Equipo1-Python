from django.db import models
from django.utils import timezone
from countryes.models import Country


class League(models.Model):
    name = models.CharField(max_length=255)
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(blank=True, null=True)
    # Una liga pertenece a un país y un país tiene muchas ligas
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return self.name
