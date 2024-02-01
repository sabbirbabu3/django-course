

from django.urls import path
from .import views
urlpatterns = [
    path('catagory/', views.catagory_view, name="catagory")
]
