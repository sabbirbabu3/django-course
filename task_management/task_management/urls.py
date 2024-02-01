
from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('taskmodel/', include('taskmodel.urls')),
    path('taskcatagory/', include('taskCategory.urls')),
]
