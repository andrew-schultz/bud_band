import urllib.request
import spotipy
from spotipy.client import SpotifyException
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from django.conf import settings

scope = 'user-library-read streaming user-read-playback-state playlist-modify-public playlist-modify-private'

client_credentials_manager = SpotifyClientCredentials(
    client_id=settings.SPOTIFY_CLIENT_ID,
    client_secret=settings.SPOTIFY_CLIENT_SECRET)

client = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

auth_manager = SpotifyOAuth(
    client_id=settings.SPOTIFY_CLIENT_ID,
    client_secret=settings.SPOTIFY_CLIENT_SECRET,
    redirect_uri='http://localhost:8000',
    scope=scope,
    show_dialog=False,
    username=client,
    cache_path='.cache-spotify')

spotify = spotipy.Spotify(auth_manager=auth_manager)


# get authorize url that you'd usually paste into the browser
#   auth_url = auth_manager.get_authorize_url()

# we need to programatically (silently if possible) "open" that url and parse the 'code' from the redirect url
#   code = auth_url.open()????
#   code = urllib.request.urlopen(auth_url)
#       this isn't quite what we want, its not giving us the url after redirect
#   ex: code = 'AQCgZg2YI48YFA-3aOq6PyLRUa_2aj7JaNOVMONrkzJ8VQ75x-bo-u3vvGtEf3GXE7kPB_If4Gsu7kXKS4MOIwfOsP4ZLwkmYaEqvPigcepb9gDijDsSGzddk_emXtpMYR40HuPEunJorpJyjS7UzySiXKaLcpV3yzlfv_HvV0GQSwRIz-_VE_tWt88KkimGHXZm3cceR8lru5cywlU2kyH61Ur-uni1CJGEIY-H89Ah7Jc4cXCFPHMfai6ktwJxyWsN19q-f69Nv7LQG_QGmaBEOLgxzIO2CoZzrS64_VTemQ'

# then we get the token from the following command:
#   token_response = auth_manager.get_access_token(code)
#   token = token_response['access_token']
#       ex: token_response = {'access_token': 'BQD-zg-_GzsjaW6xaeHvNSPLO3HY2TGTvQgihLcz_D4aJM_2bqR7pSLlliddtpGp_02dPGlUKvuzOF_B2JSbjfyjvkahDqTYidSnDF3s44SLBZwCywX9UCFw3yndyoGtXbmhehPyBZJyLTP-oOMhqQLz_68CTyBJG-HBiO07nD-5zCQtDCB2tJQCMwrQ204qpyzaSpfj8d1w0AcHs8CkECZBd-v99khZwg', 'token_type': 'Bearer', 'expires_in': 3600, 'refresh_token': 'AQDDJgtSouAe76kw89XsASZNUhXQ2MTEquADTXmlVpI-zR0gj8G9iTUT8oMWOXEbJA6XNXSLVVC5LLZeuiY2nPI_2ihwQbts5SABPvgHEIlrk_D48k6bNO8Xt2a34VKktTI', 'scope': 'playlist-modify-private playlist-modify-public streaming user-library-read user-read-playback-state', 'expires_at': 1615156130}

# init spotify with token auth
# spotify = spotipy.Spotify(auth=token)


def get_track(uri):
    try:
        track = client.track(uri)
    except SpotifyException as e:
        raise e

    return track


def add_track_to_playlist(track_uri, playlist_id):
    track_id = track_uri.split(':')[-1]

    try:
        spotify.playlist_add_items(playlist_id, [track_id], 0)
    except SpotifyException as e:
        raise e

    return True
