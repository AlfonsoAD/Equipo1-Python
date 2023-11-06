from . import models
from django.forms import ModelForm


class AnimalForm(ModelForm):
    class Meta:
        model = models.Animal
        fields = ['name', 'race']
