

from django.urls import path
from .import views
urlpatterns = [
    path('details/<int:id>/', views.CardetailsView.as_view(), name='details'),
   path('buycar/<int:id>/', views.Buycar, name='buycar'),
]
