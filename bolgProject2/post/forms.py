from django import forms
from .models import Post,Comment

class FromPost(forms.ModelForm):
    class Meta:
        model=Post
        # fields='__all__'
        exclude=['author']

class CommentsPost(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['name', 'email', 'body']
        