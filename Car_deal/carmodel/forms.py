from django import forms
from .models import CarModel,comments

class CarmodelForm(forms.ModelForm):
    class Meta:
        model=CarModel
        fields="__all__"

class CommentsForm(forms.ModelForm):
    class Meta:
        model=comments
        exclude = ['car_model'] 
