from . import models
from django.forms import ModelForm


class ConsultationForm(ModelForm):
    class Meta:
        model = models.Consultation
        fields = ['service', 'price', 'doctor', 'animal']
