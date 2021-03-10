"""budband URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from bud_band.admin import bud_band_site
from bud_band.urls import (
    account_urlpatterns,
    comment_urlpatterns,
    playlist_urlpatterns,
    spotify_song_urlpatterns,)

urlpatterns = [
    path('', bud_band_site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/v1/account/', include(account_urlpatterns)),
    path('api/v1/comment/', include(comment_urlpatterns)),
    path('api/v1/playlist/', include(playlist_urlpatterns)),
    path('api/v1/spotify_song/', include(spotify_song_urlpatterns)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
