from django.urls import path

from bud_band.views import index

urlpatterns = [
    path('', index.index, name='index'),
]