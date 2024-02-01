from django.shortcuts import render, redirect
from .forms import Task_modelForm
from. models import Task_model
# Create your views here.
def model_view(request):
   

    if request.method =='POST':
        form=Task_modelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('model')
    else:
        form=Task_modelForm()
    
    return render(request, 'model.html',{'form':form})


def update_view(request,id):
    post=Task_model.objects.get(pk=id)
    form=Task_modelForm(instance=post)
    if request.method =='POST':
        form=Task_modelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    
    return render(request, 'model.html',{'form':form})

def delete_view(request,id):
    post=Task_model.objects.get(pk=id)
    post.delete()
    return redirect('home')
    