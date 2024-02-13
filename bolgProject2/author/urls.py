
# from django.contrib import admin
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from .views import UserLogoutView




urlpatterns = [
    # path('', views.home),
    # path('home/', views.home, name='home'),
    path('register/', views.signUp_view, name='register'),
    # path('login/', views.user_login, name='login'),
    path('login/', views.UserloginView.as_view(), name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('update/', views.user_update, name='uptade'),
    path('passwrodchange/', views.user_change_password, name='changepassword'),
    path('get/', views.get_session),
]

