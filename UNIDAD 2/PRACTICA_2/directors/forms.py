from django.forms import ModelForm
from .models import Technical_Director


class DirectorForm(ModelForm):
    class Meta:
        model = Technical_Director
        fields = ['first_name', 'last_name', 'country']
