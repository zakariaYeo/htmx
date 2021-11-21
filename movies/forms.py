from django import forms
from django.forms import fields, widgets

from movies.models import Movies


class MoviesForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['name']
        widgets = {
            'name':forms.TextInput(attrs={"class":"form-control me-2","name":"name","placeholder":"Ajouter un film", "require": True})
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('Le champs requis')
        return name