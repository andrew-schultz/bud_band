from rest_framework import serializers
from bud_band.models import SpotifySong
from .comment import SpotifySongCommentSerializer
from .user import UserSerializer

class SpotifySongSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifySong
        fields = (
            'id',
            'owner',
            'description',
            'title',
            'artist',
            'album',
            'artwork',
            'uri',
            'link',
            'playlist_id',
        )
    
    owner = UserSerializer()
    playlist_id = serializers.IntegerField()


class SpotifySongExtendedSerializer(SpotifySongSerializer):
    class Meta:
        model = SpotifySong
        fields = (
            'id',
            'owner',
            'description',
            'title',
            'artist',
            'album',
            'artwork',
            'uri',
            'link',
            'comments',
            'playlist_id',
        )

    comments = SpotifySongCommentSerializer(many=True)
    playlist_id = serializers.IntegerField()


class SpotifyPostSerializer(serializers.Serializer):
    uri = serializers.CharField()
    playlist_id = serializers.IntegerField()
