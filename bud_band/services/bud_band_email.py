import re
from django.contrib.auth.models import User
from django.core.mail import send_mail, send_mass_mail
from django.template.loader import render_to_string
from budband.settings import EMAIL_HOST_USER, URL_HOST


def get_resource_type(resource):
    class_name = resource.__class__.__name__
    parts = class_name
    res_list = []
    res_list = re.findall('[A-Z][^A-Z]*', class_name)

    if 'Song' in res_list:
        return 'Song'
    else:
        return 'Playlist'


def send_budband_emails(resource, users, reporter):
    user_emails = [user.email for user in users]
    resource_type = get_resource_type(resource)

    if resource_type == 'Playlist':
        link = f'https://{URL_HOST}/api/v1/spotify_song/list/?limit=100&offset=0&playlist_id={resource.id}'
    elif resource_type == 'Song':
        link = f'https://{URL_HOST}/api/v1/spotify_song/{resource.id}/edit/'
    
    msg = f'{reporter.username} just added a new {resource_type}'
    msg_html = render_to_string(
        'email/new_object.html',
        {
            'reporter': reporter,
            'resource_type': resource_type,
            'resource': resource,
            'link': link
        }
    )

    send_mail(
        f'BudBand Update',
        msg,
        EMAIL_HOST_USER,
        user_emails,
        html_message=msg_html,
        fail_silently=False)