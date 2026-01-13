from django import forms
from django.forms import ModelForm, DateInput

from . import models
from .models import Editora


class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        exclude = ['data_criacao', 'ultima_modificacao']
        fields = '__all__'
