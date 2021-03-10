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
from bud_band.models import Playlist, SpotifySong
from bud_band.serializers.playlist import (
    PlaylistSerializer, PlaylistPostSerializer)
from bud_band.services.spotify import get_track, add_track_to_playlist, generate_playlist


class PlaylistCreateView(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser,)
    authentication_classes = (SessionAuthentication, JWTAuthentication,)

    def post(self, request):
        serializer = PlaylistPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data.get('name')
        description = serializer.validated_data.get('description', None)
        
        try:
            playlist_data = generate_playlist(name, description)
        except SpotifyException as e:
            raise e

        playlist = Playlist(name=name, description=description)
        playlist.uri = playlist_data['uri']
        playlist.link = track_info['external_urls']['spotify']

        images = playlist_info['images']
        height = 0
        for i in images:
            if i['height'] > height:
                height = i['height']
                playlist.artwork = i['url']

        playlist.save()

        serializer = PlaylistSerializer(playlist)
        return Response(serializer.data)


class PlaylistAddView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'admin/playlist/playlist.html'
    # permission_classes = (IsAuthenticated, IsAdminUser,)
    authentication_classes = (SessionAuthentication, JWTAuthentication,)

    def get(self, request):
        return Response()


class PlaylistListView(ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'admin/playlist/playlist_list.html'
    authentication_classes = (SessionAuthentication, JWTAuthentication,)

    def get(self, request):
        queryset = Playlist.objects.select_related('user').order_by('name')
        paginated_queryset = self.paginate_queryset(queryset)

        playlists = self.get_paginated_response(paginated_queryset)
        playlists = dict(playlists.data)
        playlists_data = PlaylistSerializer(playlists['results'], many=True).data

        payload = {
            'playlists_data': playlists_data,
            'next_query': playlists['next'],
            'previous_query': playlists['previous'],
            'count': playlists['count']
        }
        print('payload', payload)
        return Response(payload)


class PlaylistListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser,)
    authentication_classes = (SessionAuthentication, JWTAuthentication,)

    def get(self, request):
        queryset = Playlist.objects.select_related('user')
        paginated_queryset = self.paginate_queryset(queryset)

        playlists = self.get_paginated_response(paginated_queryset)
        playlists = dict(playlists.data)
        playlists_data = PlaylistSerializer(playlists['results'], many=True).data

        payload = {
            'playlists_data': playlists_data,
            'next_query': playlists['next'],
            'previous_query': playlists['previous'],
            'count': playlists['count']
        }
        
        return Response(payload)