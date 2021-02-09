from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from django.urls import path

from .auth import GroupAdmin, UserAdmin
from .spotify_song import SpotifySongAdmin

from bud_band.models import SpotifySong

class BudBandAdminSite(AdminSite):
    site_header = 'Bud Band Admin'
    index_title = 'Dashboard'
    site_url = None


bud_band_site = BudBandAdminSite()

bud_band_site.register(SpotifySong, SpotifySongAdmin)

# AUTHENTICATION AND AUTHORIZATION
bud_band_site.register(Group, GroupAdmin)
bud_band_site.register(User, UserAdmin)
