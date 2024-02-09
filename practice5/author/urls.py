

from django.urls import path
from .import views
urlpatterns = [
    
    path('register/',views.signup, name='register'),
    path('login/',views.user_login, name='login'),
    path('profile/',views.profile, name='profile'),
    path('logout/',views.user_logout, name='logout'),
    path('changePassword/',views.user_password_change, name='changePassword'),
    path('changePassword2/',views.user_password_change2, name='changePassword2'),
    

]
