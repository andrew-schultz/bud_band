from rest_framework import serializers
from bud_band.models import Comment
from .user import UserSerializer

class CommentSerializer(serializers.Modelserializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'text',
            'created_at',
        )
    
    user = UserSerializer()


class SpotifySongComment(CommentSerializer):
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