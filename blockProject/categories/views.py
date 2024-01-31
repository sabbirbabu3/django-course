from django.shortcuts import render, redirect
from .forms import FormCategories

# Create your views here.
def cetagory(request):
    if request.method =='POST':
        categories = FormCategories(request.POST)
        if categories.is_valid():
            categories.save()
            redirect ("category")
    else:
        categories = FormCategories()
    return render(request,'category.html',{'form':categories})