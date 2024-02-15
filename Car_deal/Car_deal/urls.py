
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('brand/<slug:model_slug>/', views.home, name='model_wise_post'),
    path('author/', include('author.urls')),
    path('brandmodel/', include('brandmodel.urls')),
    path('carmodel/', include('carmodel.urls')),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)