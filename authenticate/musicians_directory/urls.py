from django.urls import path
from .views import MusicianListView, MusicianCreateView, MusicianUpdateView, MusicianDeleteView, AlbumListView, AlbumCreateView, AlbumUpdateView, AlbumDeleteView

urlpatterns = [
    path('musicians/', MusicianListView.as_view(), name='musician_list'),
    path('musicians/new/', MusicianCreateView.as_view(), name='musician_new'),
    path('musicians/<int:pk>/edit/', MusicianUpdateView.as_view(), name='musician_edit'),
    path('musicians/<int:pk>/delete/', MusicianDeleteView.as_view(), name='musician_delete'),
 
    path('albums/', AlbumListView.as_view(), name='album_list'),
    path('albums/new/', AlbumCreateView.as_view(), name='album_new'),
    path('albums/<int:pk>/edit/', AlbumUpdateView.as_view(), name='album_edit'),
    path('albums/<int:pk>/delete/', AlbumDeleteView.as_view(), name='album_delete'),
]
