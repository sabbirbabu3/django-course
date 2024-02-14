from django.shortcuts import render, redirect
from .forms import MusicForm
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView
# Create your views hereclass LoginView(
class MusicCreateView(CreateView):
    form_class=MusicForm
    template_name='music.html'
    success_url=reverse_lazy('musician')
    def form_valid(self, form):
        form.instance.musican=self.request.user
        return super().form_valid(form)


class MusicUpdateView(UpdateView):
    form_class=MusicForm
    template_name='profile.html'
    success_url=reverse_lazy('profile')
    pk_url_kwarg='id'


class DeleteMusicView(DeleteView):
    template_name='delete.html'
    success_url=reverse_lazy('profile')
    pk_url_kwarg='id'
