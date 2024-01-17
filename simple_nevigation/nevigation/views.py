from django.shortcuts import render

# Create your views here.
def about(request):
    d ={'name': 'Sabbir','age':30}
    return render(request, 'nevigaton/about.html',d)
def contact(request):
    d={ 'courses':[
     {
        'id': 1,
        'Course': 'puython',
        'fee': 5000,
     },
       {
        'id': 2,
        'Course': 'django',
        'fee': 10000,
     },
       {
        'id': 3,
        'Course': 'C',
        'fee': 500,
     }
    ]}
        
    return render(request, 'nevigaton/contact.html',d)