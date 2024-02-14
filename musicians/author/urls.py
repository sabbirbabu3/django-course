

from django.urls import path
from .import views
urlpatterns = [
    path('profile/',views.profile, name='profile'),
    path('registration/',views.userRegistration.as_view(), name='register'),
    path('login/',views.UserLogin.as_view(), name='login'),
    path('logout/',views.user_logout, name='logout'),
    path('update/<int:id>/',views.user_logout, name='logout'),
    path('delete/<int:id>/',views.user_logout, name='logout'),
    
]
