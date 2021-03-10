from rest_framework import serializers
from bud_band.models import Playlist
from .user import UserSerializer


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = (
            'id',
            'user',
            'name',
            'description',
            'artwork',
            'uri',
        )
    
    user = UserSerializer()


class PlaylistPostSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField(required=False)
