

from django.urls import path
from .import views
urlpatterns = [
    path('post/', views.PostView, name='frompost' ),
    path('edit/<int:id>', views.editView, name='edit' ),
    path('delete/<int:id>', views.deleteView, name='delete' ),
    
]
