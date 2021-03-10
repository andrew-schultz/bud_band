import re
from django.contrib.auth.models import User
from django.core.mail import send_mail, send_mass_mail
from budband.settings import EMAIL_HOST_USER


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
    # lets include a link eh? That would be dope
    # look into best practice, but maybe we can figure out a little formatting brilliance too?
    send_mail(
        f'BudBand Update',
        f'{reporter.username} just added a new {resource_type}',
        EMAIL_HOST_USER,
        user_emails,
        # ['as173171@gmail.com'],
        fail_silently=False)