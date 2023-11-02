from django.db import models
from django.utils import timezone


class Technical_Director(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
