

from django.urls import path
from .import views
urlpatterns = [
    
    path('musician/', views.MusicCreateView.as_view(), name='musician'),
    path('update/<int:id>/',views.MusicUpdateView.as_view(), name='update'),
    path('delete/<int:id>/',views.DeleteMusicView.as_view(), name='delete'),
]
