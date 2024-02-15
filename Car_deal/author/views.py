from django.shortcuts import render,redirect
from .forms import UserRegistrationForm,ChangeUserForm
from django.views.generic import CreateView,DeleteView,UpdateView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.models import User

# Create your views here.
class UserRegistrationView(CreateView):
    form_class=UserRegistrationForm
    template_name='user.html'
    success_url=reverse_lazy('register')
    def form_valid(self, form):
        return super().form_valid(form)
    def get_context_data(self, **kwargs) :
        context=super().get_context_data(**kwargs)
        context['type']='register'
        return context

class UserLoginView(LoginView):
    template_name='user.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    
    def get_context_data(self, **kwargs) :
        context=super().get_context_data(**kwargs)
        context['type']='login'
        return context

class UserUpdateView(UpdateView):
    model=User
    form_class=ChangeUserForm
    template_name='user.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    pk_url_kwarg='id'
    def get_context_data(self, **kwargs) :
        context=super().get_context_data(**kwargs)
        context['type']='update'
        return context
    

def ProfileView(request):
    return render(request, 'profile.html')

def user_logout(request):
    logout(request)
    return redirect('login')