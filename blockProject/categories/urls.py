

from django.urls import path
from .import views
urlpatterns = [
    path('category/', views.cetagory, name='category'),
    
]
