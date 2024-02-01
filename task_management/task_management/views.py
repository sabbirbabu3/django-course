from django.shortcuts import render
from taskmodel.models import Task_model
def home(request):
    data=Task_model.objects.all()
    return render(request, 'home.html',{'data':data})