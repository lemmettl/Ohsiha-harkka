from django import forms
from .models import Arvostelu

class ArvosteluForm(forms.ModelForm):
    class Meta:
        model = Arvostelu
        fields = ['otsikko', 'arvosana', 'kommentti']
