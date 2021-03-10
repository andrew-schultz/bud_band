from django.contrib import admin
from django.forms.widgets import HiddenInput
from django.utils.html import format_html
from bud_band.models import SpotifySong, Playlist
from bud_band.services.spotify import generate_playlist


class SongInline(admin.TabularInline):
    model = SpotifySong
    readonly_fields = (
        'title',
        'artist',
        'owner'
    )
    fields = () + readonly_fields

    extra = 0

    def has_change_permission(self, request, obj=None):
        return False


class PlaylistAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )

    list_display = (
        'name',
        'user',
        'uri',
    )

    readonly_fields = (
        'name',
        'user',
        'description',
        'uri',
    )

    fields = () + readonly_fields

    inlines = [SongInline,]

    def get_readonly_fields(self, request, obj=None):
        if obj is None:
            return ()
        
        return self.readonly_fields

    def spotify_link(self, obj):
        if obj and obj.link:
            return format_html('<a href="{0}" target="_blank">Open in Spotify</a>'.format(obj.link))
        return None
    spotify_link.short_description = 'Link'

    def save_model(self, request, obj, form, change):
        name = form.cleaned_data.get('name', None)
        description = form.cleaned_data.get('description', None)
        uri = form.cleaned_data.get('uri', None)

        if not uri:
            playlist = generate_playlist(name, description)
            obj.uri = playlist['uri']

            images = playlist['images']
            height = 0
            for i in images:
                if i['height'] > height:
                    height = i['height']
                    obj.artwork = i['url']

        if not obj.user_id:
            obj.user_id = request.user.id

        super().save_model(request, obj, form, change)


__all__ = [
    'PlaylistAdmin'
]