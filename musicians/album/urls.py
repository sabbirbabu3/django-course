

from django.urls import path
from .import views
urlpatterns = [
    path('album/',views.AlbumView.as_view(), name='album'),
    path('update/<int:id>/',views.MusicUpdateView.as_view(), name='update'),
    path('delete/<int:id>/',views.DeleteMusicView.as_view(), name='delete'),
    
]
