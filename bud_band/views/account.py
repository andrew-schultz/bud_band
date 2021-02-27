import jwt

from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from bud_band.auth import JWTAuthentication
from bud_band.models import SpotifySong
from bud_band.serializers.account import LoginSerializer, LoginResponseSerializer
from bud_band.serializers.spotify_song import SpotifySongSerializer
from bud_band.utils import create_api_token



class LoginView(APIView):
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
