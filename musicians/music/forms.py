from django import forms
from .models import Musician

class MusicForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'
