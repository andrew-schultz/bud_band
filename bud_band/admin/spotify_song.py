from django.contrib import admin
from django.forms.widgets import HiddenInput
from django.utils.html import format_html
from bud_band.models import SpotifySong, SpotifySongComment
from bud_band.services.spotify import get_track


class CommentInline(admin.StackedInline):
    model = SpotifySongComment
    template = 'admin/comment_inline.html'
    readonly_fields = (
        'created_at',
    )
    fields = (
        'text',
        'user',
    ) + readonly_fields

    def has_change_permission(self, request, obj=None):
        return False

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs['initial'] = request.user.id
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_extra(self, request, obj=None, **kwargs):
        if not obj:
            extra = 0
        else:
            extra = 1
        return extra


class SpotifySongAdmin(admin.ModelAdmin):
    search_fields = (
        'title',
        'artist',
        'album',
    )

    list_display = (
        'title',
        'artist',
        'album',
        'owner',
        'image_thumb',
    )

    readonly_fields = (
        'title',
        'artist',
        'album',
        'spotify_link',
        'image_tag',
        'owner',
    )

    fields = (
        'uri',
    ) + readonly_fields

    inlines = [CommentInline,]

    def get_readonly_fields(self, request, obj=None):
        if obj is None:
            return ()
        
        readonly_fields = self.readonly_fields + ('uri',)
        return readonly_fields

    def get_fields(self, request, obj=None):
        if obj is None:
            return ('uri',)
        return self.fields

    def spotify_link(self, obj):
        if obj and obj.link:
            return format_html('<a href="{0}" target="_blank">Open in Spotify</a>'.format(obj.link))
        return None
    spotify_link.short_description = 'Link'

    def image_tag(self, obj):
        if obj and obj.artwork:
            return format_html('<img src="{0}" style="width: 300px; height: 300px;" />'.format(obj.artwork))
        return None
    image_tag.short_description = 'Image'

    def image_thumb(self, obj):
        if obj and obj.artwork:
            return format_html('<img src="{0}" style="width: 45px; height: 45px;" />'.format(obj.artwork))
        return None
    image_thumb.short_description = 'Image'

    def save_model(self, request, obj, form, change):
        uri = form.cleaned_data.get('uri', None)

        if uri:
            track_info = get_track(uri)

            if track_info:
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
                    
        
        if not obj.owner_id:
            obj.owner_id = request.user.id

        super().save_model(request, obj, form, change)

    def save_related(self, request, form, formsets, change):
        for formset in formsets:
            print('formset', formset)

        super().save_related(request, form, formsets, change)


__all__ = [
    'SpotifySongAdmin'
]