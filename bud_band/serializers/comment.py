from rest_framework import serializers
from bud_band.models import Comment, SpotifySongComment
from .user import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'text',
            'created_at',
        )
    
    user = UserSerializer()


class SpotifySongCommentSerializer(CommentSerializer):
    class Meta:
        model = SpotifySongComment
        fields = (
            'id',
            'user',
            'text',
            'created_at',
            'spotify_song_id',
        )
    
    spotify_song_id = serializers.IntegerField()


class SpotifyCommentPostSerializer(serializers.Serializer):
    text = serializers.CharField()
    spotify_song_id = serializers.IntegerField()
