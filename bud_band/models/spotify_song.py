from django.db import models
from django.contrib.auth.models import User
from bud_band.models.playlist import Playlist


class SpotifySong(models.Model):
    "A reference to a Spotify track"

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='spotify_songs')
    description = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    artist = models.CharField(max_length=255, blank=True, null=True)
    album = models.CharField(max_length=255, blank=True, null=True)
    artwork = models.URLField(max_length=255, blank=True, null=True)
    uri = models.CharField(max_length=255, blank=True, null=True)
    link = models.URLField(max_length=255, blank=True, null=True)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name='songs', blank=True, null=True)


def build_uri_from_link(link):
    # sample link pattern: https://open.spotify.com/track/4XoYeolVYTiddO9wZLXLgl?si=V6s-mtoZSYaqrG8yHWY5uA
    # sample uri pattern: spotify:track:4XoYeolVYTiddO9wZLXLgl
    link_parts = link.split('/')
    key = link_parts[-1].split('?')[0]
    uri = f'spotify:track:{key}'
    return uri