from django.shortcuts import render
from album.models import AlbumModel
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView
from album.forms import AlbumForm

# Create your views here.
def home(request):
    data=AlbumModel.objects.all()
    return render(request, 'home.html', {'data': data})


class MusicUpdateView(UpdateView):
    model = AlbumModel
    form_class = AlbumForm
    template_name = 'profile.html'
    pk_url_kwarg = 'id'  # Correct attribute name
    success_url = reverse_lazy('profile')


class DeleteMusicView(DeleteView):
    model = AlbumModel
    template_name='delete.html'
    success_url =reverse_lazy('profile')
    pk_url_kwarg= 'id'