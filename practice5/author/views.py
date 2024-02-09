from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required  # Import the decorator
from .forms import RegistrationForm

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful")
            return redirect('register')
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form, 'type': 'register'})

@login_required  # Apply the decorator to restrict access to logged-in users only
def profile(request):
    return render(request, 'profile.html')

@login_required  # Apply the decorator to restrict access to logged-in users only
def user_logout(request):
    logout(request)
    messages.success(request, 'logout successfully')
    return redirect('login')

@login_required  # Apply the decorator to restrict access to logged-in users only
def user_password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password changed successfully')
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'signup.html', {'form': form, 'type': 'changePassword'})

@login_required  # Apply the decorator to restrict access to logged-in users only
def user_password_change2(request):
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password changed successfully')
            return redirect('profile')
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, 'signup.html', {'form': form, 'type': 'changePassword'})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=name, password=user_pass)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful")
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'signup.html', {'form': form, 'type': 'login'})
