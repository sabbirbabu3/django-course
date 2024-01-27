# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, ),  # Add this line for the root path
    path('home/', views.home, name='homepage'),
    path('table/', views.table, name='table'),
    path('delete/<int:roll>', views.delete_studetTables, name='delete_studetTables'),
]
