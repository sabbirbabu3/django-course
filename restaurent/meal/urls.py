

from django.urls import path
from . import views

urlpatterns = [
    
    # path('', views.home ),
    path('meals/', views.meals, name="meals" ),
]
