from django.shortcuts import render, redirect
from .import forms
from .import models

# Create your views here.
def PostView(request):

    if request.method == 'POST':
        postFrom=forms.FromPost(request.POST)
        if postFrom.is_valid():
            postFrom.save()
            return redirect("frompost")
    else:
        postFrom=forms.FromPost()
    return render(request, 'post.html', {'form': postFrom})


def editView(request,id):
    post=models.Post.objects.get(pk=id)
    postFrom=forms.FromPost(instance=post)
    
    if request.method == 'POST':
        postFrom=forms.FromPost(request.POST,instance=post)
        if postFrom.is_valid():
            postFrom.save()
            return redirect('home')
    
    return render(request, 'post.html', {'form': postFrom})

def deleteView(request,id):
    data=models.Post.objects.get(pk=id)
    data.delete()
    return redirect('home')

