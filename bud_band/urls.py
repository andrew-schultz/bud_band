from django.urls import path

from bud_band.views import account, comment, spotify_song


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

spotify_song_urlpatterns = [
    path('<int:id>/', spotify_song.SpotifySongAPIView.as_view(), name='spotify-song'),
    path('<int:id>/edit/', spotify_song.SpotifySongEditView.as_view(), name='spotify-song-edit'),
    path('create/', spotify_song.SpotifySongAddView.as_view(), name='spotify-song-add'),
    path('', spotify_song.SpotifySongCreateView.as_view(), name='spotify-song-create'),
    path('list/', spotify_song.SpotifySongListView.as_view(), name='spotify-song-list'),
    path('list_api/', spotify_song.SpotifySongListAPIView.as_view(), name='spotify-song-list-api')
]