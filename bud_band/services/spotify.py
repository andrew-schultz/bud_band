import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.conf import settings

scope = 'user-library-read streaming user-read-playback-state'
client_credentials_manager = SpotifyClientCredentials(
    client_id=settings.SPOTIFY_CLIENT_ID,
    client_secret=settings.SPOTIFY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_track(uri):
    try:
        track = sp.track(uri)
    except SpotifyException as e:
        raise e

    return track
