from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from bud_band.auth import JWTAuthentication
from bud_band.models import SpotifySongComment
from bud_band.serializers.comment import (
    SpotifyCommentPostSerializer, SpotifySongCommentSerializer,)


class SpotifyCommentView(APIView):
    authentication_classes = (SessionAuthentication, JWTAuthentication)

    def post(self, request):
        serializer = SpotifyCommentPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        comment = SpotifySongComment.objects.create(user=request.user, **serializer.data)
        serializer = SpotifySongCommentSerializer(comment)
        return Response(serializer.data)
