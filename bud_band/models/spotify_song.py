from django.db import models
from django.contrib.auth.models import User

# hook up to the spotify api
# - new object form will accept a spotify_uri
#   - look up in spotify api with uri
#   - hopefully it returns artist, title, album, artwork (etc...)


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
