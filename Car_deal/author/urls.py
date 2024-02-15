

from django.urls import path
from .import views
urlpatterns = [
    path('profile/',views.ProfileView, name='profile'),
    path('logout/',views.user_logout, name='logout'),
    path('register/',views.UserRegistrationView.as_view(), name='register'),
    path('login/',views.UserLoginView.as_view(), name='login'),
   path('update/<int:id>/', views.UserUpdateView.as_view(), name='update'),

]
