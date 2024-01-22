
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home ),
    path('meal/', include('meal.urls')),
     path('about_us/', include('about_us.urls')),

    path('home/', views.main, name="home" ),
]
