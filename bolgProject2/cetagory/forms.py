from django import forms
from .models import Cetagories

class FormCategories(forms.ModelForm):
    class Meta:
        model=Cetagories
        fields='__all__'