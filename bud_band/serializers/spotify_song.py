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
        )
    
    owner = UserSerializer()


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
        )

    comments = SpotifySongCommentSerializer(many=True)


class SpotifyPostSerializer(serializers.Serializer):
    uri = serializers.CharField()
