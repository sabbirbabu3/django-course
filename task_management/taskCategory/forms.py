from django import forms
from .models import Category_model

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category_model
        fields = "__all__"

