from django import forms
from django.forms import ModelForm, DateInput

from . import models
from .models import Autor


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        exclude = ['data_criacao', 'ultima_modificacao']
        fields = '__all__'