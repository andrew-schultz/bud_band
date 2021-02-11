from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
        abstract = True


class SpotifySongComment(Comment):
    spotify_song = models.ForeignKey('SpotifySong', on_delete=models.CASCADE, related_name='comments')
