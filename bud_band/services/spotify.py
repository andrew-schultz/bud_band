import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

scope = 'user-library-read streaming user-read-playback-state'
client_credentials_manager = SpotifyClientCredentials(
    client_id="ff02482e17584e4eb9c99c2712ccd08d",
    client_secret="bbe3cc580a7e4adba8b30ad31b609bc0")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_track(uri):
    try:
        track = sp.track(uri)
    except SpotifyException as e:
        raise e

    print('track is', track)
    return track
