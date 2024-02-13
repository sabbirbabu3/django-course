from django.shortcuts import render
from post.models import Post
from cetagory.models import Cetagories

def home(request, category_slug=None):
    data=Post.objects.all()
    if category_slug is not None:
        cetagory=Cetagories.objects.get(slug=category_slug)
        data=Post.objects.filter(categories  = cetagory)
    cetagories=Cetagories.objects.all()
    

    return render(request, 'home.html',{'data':data, 'category':cetagories})