from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import StudentModel

# Create your views here.
def home(request):
    if request.method =='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    else:
         form=StudentForm()

    return render(request, 'home.html',{'form':form})

def table(request):
    data=StudentModel.objects.all()
    return render(request, 'table.html',{'data':data})

def delete_studetTables(request,roll):
 
        student = StudentModel.objects.get(pk=roll)
        student.delete()
        return redirect('homepage')  # Redirect to the homepage after successful deletion
   