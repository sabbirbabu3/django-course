from django import forms
from .models import Album_Model
class Album_Form(forms.ModelForm):
    class Meta:
        model=Album_Model
        fields="__all__"
        
