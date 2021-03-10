import jwt

from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.urls import reverse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication
from rest_framework.renderers import TemplateHTMLRenderer

from bud_band.auth import JWTAuthentication
from bud_band.models import SpotifySong
from bud_band.serializers.account import LoginSerializer, LoginResponseSerializer
from bud_band.serializers.spotify_song import SpotifySongSerializer
from bud_band.utils import create_api_token



class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username').strip()
        password = serializer.validated_data.get('password').strip()
        
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            payload = {
                'id': user.id,
                'uuid': user.profile.uuid_encoded
            }
            token = create_api_token(payload)
        else:
            raise NotFound()

        return Response(LoginResponseSerializer({'token': token}).data)


class LoginTemplateView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'admin/account/login.html'

    def get(self, request):
        if request.user and request.user.username:
            return redirect('/api/v1/playlist/list/?limit=100&offset=0')

        return Response()
