from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Musician, Album
from .forms import MusicianForm, AlbumForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class MusicianListView(ListView):
    model = Musician
    template_name = 'musician_list.html'

class MusicianCreateView(LoginRequiredMixin, CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician_form.html'
    success_url = reverse_lazy('musician_list')

class MusicianUpdateView(LoginRequiredMixin, UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician_form.html'
    success_url = reverse_lazy('musician_list')

class MusicianDeleteView(LoginRequiredMixin, DeleteView):
    model = Musician
    template_name = 'musician_confirm_delete.html'
    success_url = reverse_lazy('musician_list')

# Similarly for Album

class AlbumListView(ListView):
    model = Album
    template_name = 'album_list.html'
    context_object_name = 'albums'

class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album_form.html'
    success_url = reverse_lazy('album_list')

class AlbumUpdateView(LoginRequiredMixin, UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album_form.html'
    success_url = reverse_lazy('album_list')

class AlbumDeleteView(LoginRequiredMixin, DeleteView):
    model = Album
    template_name = 'album_confirm_delete.html'
    success_url = reverse_lazy('album_list')