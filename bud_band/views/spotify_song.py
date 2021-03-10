from spotipy.client import SpotifyException
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.renderers import TemplateHTMLRenderer
from django.conf import settings
from bud_band.auth import JWTAuthentication
from bud_band.models import SpotifySong, Playlist
from bud_band.models.spotify_song import build_uri_from_link
from bud_band.serializers.spotify_song import (
    SpotifySongSerializer, SpotifySongExtendedSerializer, SpotifyPostSerializer)
from bud_band.services.spotify import get_track, add_track_to_playlist, build_id_from_uri


class SpotifySongAPIView(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser,)
    authentication_classes = (SessionAuthentication, JWTAuthentication,)

    def get(self, request, id):
        try:
            song = SpotifySong.objects.prefetch_related('comments').get(id=id)
        except SpotifySong.DoesNotExist:
            raise NotFound()

        serializer = SpotifySongExtendedSerializer(song)
        return Response(serializer.data)


class SpotifySongCreateView(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser,)
    authentication_classes = (SessionAuthentication, JWTAuthentication,)

    def post(self, request):

        serializer = SpotifyPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        uri = serializer.validated_data.get('uri')
        playlist_id = serializer.validated_data.get('playlist_id')

        try:
            playlist = Playlist.objects.get(id=playlist_id)
        except Playlist.DoesNotExist as e:
            raise e

        uri = build_uri_from_link(uri)
        try:
            track_info = get_track(uri)
        except SpotifyException as e:
            raise e

        song = SpotifySong(uri=uri, owner_id=request.user.id, playlist=playlist)
        song.title = track_info['name']
        song.artist = track_info['artists'][0]['name']
        song.album = track_info['album']['name']
        song.link = track_info['external_urls']['spotify']

        images = track_info['album']['images']
        height = 0
        for i in images:
            if i['height'] > height:
                height = i['height']
                song.artwork = i['url']

        song.save()
        playlist_id = build_id_from_uri(playlist.uri)
        add_track_to_playlist(song.uri, playlist_id)

        serializer = SpotifySongExtendedSerializer(song)
        return Response(serializer.data)


class SpotifySongAddView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'admin/spotify_song/spotify_song.html'
    # permission_classes = (IsAuthenticated, IsAdminUser,)
    authentication_classes = (SessionAuthentication, JWTAuthentication,)

    def get(self, request):
        playlist_id = request.query_params.get('playlist_id', '')
        payload = {
            'song_data': {},
            'comments': [],
            'playlist_id': playlist_id
        }
        return Response(payload)


class SpotifySongEditView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'admin/spotify_song/spotify_song.html'
    # permission_classes = (IsAuthenticated, IsAdminUser,)
    authentication_classes = (SessionAuthentication, JWTAuthentication,)
    serializer_class = SpotifySongExtendedSerializer

    def get(self, request, id):
        try:
            song = SpotifySong.objects.prefetch_related('comments').get(id=id)
        except SpotifySong.DoesNotExist:
            raise NotFound()

        serializer = SpotifySongExtendedSerializer(song)
        song_data = serializer.data
        print('song_data', song_data['playlist_id'])
        payload = {
            'song_data': song_data,
            'comments': song_data['comments'],
            'playlist_id': song_data['playlist_id']}
        return Response(payload)


class SpotifySongListView(ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'admin/spotify_song/spotify_song_list.html'
    authentication_classes = (SessionAuthentication, JWTAuthentication,)

    def get(self, request):
        queryset = SpotifySong.objects

        if request.query_params.get('playlist_id'):
            playlist_id = request.query_params.get('playlist_id')
            queryset = queryset.filter(playlist_id=playlist_id)

        queryset = queryset.select_related('owner').order_by('-id')
        paginated_queryset = self.paginate_queryset(queryset)

        songs = self.get_paginated_response(paginated_queryset)
        songs = dict(songs.data)
        songs_data = SpotifySongSerializer(songs['results'], many=True).data

        payload = {
            'playlist_id': playlist_id,
            'songs_data': songs_data,
            'next_query': songs['next'],
            'previous_query': songs['previous'],
            'count': songs['count']
        }
        return Response(payload)


class SpotifySongListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser,)
    authentication_classes = (SessionAuthentication, JWTAuthentication,)

    def get(self, request):
        queryset = SpotifySong.objects
        
        if request.query_params.get('playlist_id'):
            playlist_id = request.query_params.get('playlist_id')
            queryset = queryset.filter(playlist_id=playlist_id)

        queryset = queryset.select_related('owner').order_by('-id')
        paginated_queryset = self.paginate_queryset(queryset)

        songs = self.get_paginated_response(paginated_queryset)
        songs = dict(songs.data)
        songs_data = SpotifySongSerializer(songs['results'], many=True).data

        payload = {
            'playlist_id': playlist_id,
            'songs_data': songs_data,
            'next_query': songs['next'],
            'previous_query': songs['previous'],
            'count': songs['count']
        }
        return Response(payload)
