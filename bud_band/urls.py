from django.urls import path

from bud_band.views import account, comment, playlist, spotify_song


# index_urlpatterns = [
#     # path('', index.index, name='index'),
# ]

account_urlpatterns = [
    path('login_token/', account.LoginAPIView.as_view(), name='api-login'),
    path('login/', account.LoginTemplateView.as_view(), name='api-login-view'),
]

comment_urlpatterns = [
    path('', comment.SpotifyCommentView.as_view(), name='comment'),
]

playlist_urlpatterns = [
    # path('<int:id>/', playlist.PlaylistAPIView.as_view(), name='playlist'),
    # path('<int:id>/edit/', playlist.PlaylistEditView.as_view(), name='playlist-edit'),
    path('create/', playlist.PlaylistAddView.as_view(), name='playlist-add'),
    path('', playlist.PlaylistCreateView.as_view(), name='playlist-create'),
    path('list/', playlist.PlaylistListView.as_view(), name='playlist-list'),
    path('list_api/', playlist.PlaylistListAPIView.as_view(), name='playlist-list-api')
]

spotify_song_urlpatterns = [
    path('<int:id>/', spotify_song.SpotifySongAPIView.as_view(), name='spotify-song'),
    path('<int:id>/edit/', spotify_song.SpotifySongEditView.as_view(), name='spotify-song-edit'),
    path('create/', spotify_song.SpotifySongAddView.as_view(), name='spotify-song-add'),
    path('', spotify_song.SpotifySongCreateView.as_view(), name='spotify-song-create'),
    path('list/', spotify_song.SpotifySongListView.as_view(), name='spotify-song-list'),
    path('list_api/', spotify_song.SpotifySongListAPIView.as_view(), name='spotify-song-list-api')
]