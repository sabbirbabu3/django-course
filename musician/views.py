from django.shortcuts import render, redirect
from .models import Musician_Model
from .forms import Music_Form
# Create your views here.
def musicView(request):
    if request.method == 'POST':
        form = Music_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form=Music_Form()

    return render(request, 'music.html',{'form':form})
def update(request,id):
    post=Musician_Model.objects.get(pk=id)
    form = Music_Form(instance=post)
    if request.method == 'POST':
        form = Music_Form(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
       

    return render(request, 'music.html',{'form':form})