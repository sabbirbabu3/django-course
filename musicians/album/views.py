from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView
# from models import AlbumModel
from .forms import AlbumForm
from .models import AlbumModel

# Create your views here.
class AlbumView(CreateView):
    form_class = AlbumForm
    template_name="album.html"
    success_url = reverse_lazy('album')
    def form_valid(self, form):
        # form.instance.album_name=self.request.user
        return super().form_valid(form)

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
