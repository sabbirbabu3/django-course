from django import forms
from .import models

class Music_Form(forms.ModelForm):
    
    class Meta:
        model = models.Musician_Model
        fields = "__all__"
