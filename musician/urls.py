

from django.urls import path
from .import views

urlpatterns = [
    
    path('music/', views.musicView, name='music'),
    path('update/<int:id>/', views.update, name='upgrade'),
    
]
