from . import models
from django.forms import ModelForm


class TeamForm(ModelForm):
    class Meta:
        model = models.Team
        fields = ['name', 'league', 'count_players', 'technical_director']
