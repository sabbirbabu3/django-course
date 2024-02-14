
from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # path('', views.postTable),
    path('', include('album.urls')),
    path('musician/', include('music.urls')),
    path('author/', include('author.urls')),
    path('update/<int:id>/',views.MusicUpdateView.as_view(), name='update'),
    path('delete/<int:id>/',views.DeleteMusicView.as_view(), name='delete'),
]
