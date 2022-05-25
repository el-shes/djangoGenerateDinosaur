from django import forms
from .models import GeneratedDino


class GeneratedDinoForm(forms.ModelForm):
    class Meta:
        model = GeneratedDino
        fields = ['name']
