from django.contrib import admin
from bud_band.models import SpotifySong
from bud_band.services.spotify import get_track


class SpotifySongAdmin(admin.ModelAdmin):
    search_fields = ('title', 'artist', 'album',)
    list_display = ('title', 'artist', 'album', 'owner',)
    readonly_fields = ('title', 'artist', 'album', 'owner',)

    def save_model(self, request, obj, form, change):
        uri = form.cleaned_data.get('uri', None)

        if uri:
            track_info = get_track(uri)

            if track_info:
                print('track_info')
                obj.title = track_info['name']
                obj.artist = track_info['artists'][0]['name']
                obj.album = track_info['album']['name']
                obj.link = track_info['external_urls']['spotify']

                images = track_info['album']['images']
                height = 0
                for i in images:
                    if i['height'] > height:
                        height = i['height']
                        obj.artwork = i['url']
                    
            # spotify:track:1jzZHQtZMrxmu8SpKVG7z4
        
        if not obj.owner_id:
            obj.owner_id = request.user.id

        super().save_model(request, obj, form, change)


__all__ = [
    'SpotifySongAdmin'
]