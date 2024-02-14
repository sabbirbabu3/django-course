from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.views import  LoginView, LogoutView
from django.views.generic import CreateView,UpdateView,DeleteView
from .forms import Register
from django.urls import reverse_lazy
from django.contrib.auth import  logout
from album.models import AlbumModel

# Create your views here.
def profile(request):
    data=AlbumModel.objects.all()
    return render(request, 'profile.html', {'data': data})
    

class userRegistration(CreateView):
    form_class=Register
    template_name='user.html'
    success_url=reverse_lazy('register')
    def form_valid(self, form):
        return super().form_valid(form)
    # for type
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['type']='register'                
        return context
    
class UserLogin(LoginView):
    template_name='user.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['type']='login'                
        return context
def user_logout(request):
    logout(request)
    return redirect('login')

