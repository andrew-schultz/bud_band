from spotipy.client import SpotifyException
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.renderers import TemplateHTMLRenderer
from bud_band.auth import JWTAuthentication
from bud_band.models import SpotifySong
from bud_band.models.spotify_song import build_uri_from_link
from bud_band.serializers.spotify_song import (
    SpotifySongSerializer, SpotifySongExtendedSerializer, SpotifyPostSerializer)
from bud_band.services.spotify import get_track


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
        uri = build_uri_from_link(uri)
        try:
            track_info = get_track(uri)
        except SpotifyException as e:
            raise e

        song = SpotifySong(uri=uri, owner_id=request.user.id)
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
        serializer = SpotifySongExtendedSerializer(song)
        return Response(serializer.data)


class SpotifySongAddView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'admin/spotify_song/spotify_song.html'
    # permission_classes = (IsAuthenticated, IsAdminUser,)
    authentication_classes = (SessionAuthentication, JWTAuthentication,)

    def get(self, request):
        payload = {'song_data': {}, 'comments': []}
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
        payload = {'song_data': song_data, 'comments': song_data['comments']}
        return Response(payload)
