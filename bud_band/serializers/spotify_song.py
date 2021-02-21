from rest_framework import serializers
from bud_band.models import SpotifySong
from .user import UserSerializer

class SpotifySongSerializer(serializers.Modelserializer):
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