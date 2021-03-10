from django.db import models
from django.contrib.auth.models import User

class Playlist(models.Model):
    "A reference to a Spotify playlist"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')
    description = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, default='')
    uri = models.CharField(max_length=255, blank=True, null=True)
    link = models.URLField(max_length=255, blank=True, null=True)
    artwork = models.URLField(max_length=255, blank=True, null=True)

    @property
    def spotify_id(self):
        spotify_id = self.uri.split(':')[-1]
        return spotify_id