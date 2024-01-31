from django.shortcuts import render,redirect
from album.models import Album_Model
from musician.forms import Music_Form


def home(request):
    post=Album_Model.objects.all()

    return render(request, 'home.html',{'form':post})