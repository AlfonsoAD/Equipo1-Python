from django.db import models
from django.utils import timezone


class Country(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    create_date = models.DateTimeField(
        default=timezone.now, blank=False, null=False)
    update_date = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name
