from django.shortcuts import render, redirect
from .models import Album_Model
from .forms import Album_Form
# Create your views here.
def album_view(request):
    if request.method == 'POST':
        form = Album_Form(request.POST)
        if form.is_valid():
            form.save()
            print("Form saved successfully")
            return redirect('album')
        else:
            print("Form is not valid. Errors:", form.errors)
    else:
        form = Album_Form()

    return render(request, 'album.html', {'form': form})


def album_update(request,id):
    post = Album_Model.objects.get(pk=id)
    form = Album_Form(instance=post)

    if request.method == 'POST':
        form = Album_Form(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'album.html', {'form': form})


def delete_view(request,id):
    post=Album_Model.objects.get(pk=id)
    post.delete()
    return redirect('home')