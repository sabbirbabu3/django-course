from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import login,logout,update_session_auth_hash,authenticate
from django.contrib.auth.views import LoginView,LogoutView
from .import forms
from django.contrib.auth.decorators import login_required
from post.models import Post
from django.urls import reverse_lazy
from django.http import HttpResponse
# Create your views here.


def signUp_view(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request,"Your account has been registered")
            form.save()
            # Redirect to the 'home' view after successful form submission
            return redirect('register')
    else:
        form = forms.RegisterForm()

    return render(request, 'signup.html', {'form': form, 'type':'register'})

def user_login(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']  # Corrected key name
            password = form.cleaned_data['password']  # Corrected key name
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form, 'type':'login'})

class UserloginView(LoginView):
    template_name='login.html'
    # success_url=reverse_lazy('profile')
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request, 'login successful')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, 'please enter the correct username')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['type']='login'
        return context
                       

   
    

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    data=Post.objects.filter(author=request.user)
    return render(request, 'profile.html', {'data':data})



def set_session(self, request):
    # Example of setting a session variable
    request.session['user_id'] = request.user.id
    return redirect('profile')

def get_session(self, request):
    # Example of retrieving a session variable
    user_id = request.session.get('user_id')
    
    if user_id:
        # Session variable exists, do something
        request.session.modified = True
        return render(request, 'login.html')
    else:
        return HttpResponse("Your session has expired or does not exist")



#class base logout
class UserLogoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('home')


@login_required
def user_update(request):
    if request.method == 'POST':
        form = forms.user_update_form(request.POST, instance=request.user)
        if form.is_valid():
            messages.success(request,"Your account has been registered")
            form.save()
            # Redirect to the 'home' view after successful form submission
            return redirect('profile')
    else:
        form = forms.user_update_form(instance=request.user)

    return render(request, 'signup.html', {'form': form, 'type':'update'})


def user_change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)  # Assign the form instance to the 'form' variable here

    return render(request, 'login.html', {'form': form, 'type': 'password_change'})

