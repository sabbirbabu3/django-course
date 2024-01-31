

from django.urls import path
from .import views

urlpatterns = [
    
    path('album/', views.album_view, name='album'),
    path('update/<int:id>/', views.album_update, name='update'),
    path('delete/<int:id>/', views.delete_view, name='delete'),
    
]
