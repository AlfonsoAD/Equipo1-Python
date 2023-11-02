from . import models
from django.forms import ModelForm


class LeagueForm(ModelForm):
    class Meta:
        model = models.League
        fields = ['name', 'country']
