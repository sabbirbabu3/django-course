

from django.urls import path
from . import views
urlpatterns = [
    path('model/', views.model_view, name="model"),
    path('update/<int:id>/', views.update_view, name="update"),
    path('delete/<int:id>/', views.delete_view, name="delete"),
]
