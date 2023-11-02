from . import models
from django.forms import ModelForm


class PlayerForm(ModelForm):
    class Meta:
        model = models.Player
        fields = ['first_name', 'last_name', 'age',
                  'position', 'team', 'shirt_number', 'country']
