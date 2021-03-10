import re
from django.contrib.auth.models import User
from django.core.mail import send_mail, send_mass_mail


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
    
    send_mail(
        f'BudBand Update',
        f'{reporter.username} just added a new {resource_type}',
        'randlespelledlikehandle@gmail.com',
        user_emails)