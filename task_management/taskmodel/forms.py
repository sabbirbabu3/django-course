from django import forms
from .models import Task_model
class Task_modelForm(forms.ModelForm):
    class Meta:
        model=Task_model
        fields="__all__"