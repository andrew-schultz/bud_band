"""
Django settings for budband project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
import environ
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'ca916cb9s(i#_c%7ie3gpf79tjat*w(98%1wg_sj_k+9^$(^bk'

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = int(os.environ.get("DEBUG", default=0))

# 'DJANGO_ALLOWED_HOSTS' should be a single string of hosts with a space between each.
# For example: 'DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]'
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = []

ENV = os.environ.get("ENV")

if ENV and ENV != 'Dev':
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    # SECURE_PROXY_SSL_HEADER = os.environ.get("SECURE_PROXY_SSL_HEADER").split(" ")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'webpack_loader',
    'bud_band',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'budband.urls'

cors_rule = os.environ.get('CORS_RULE')
CORS_ORIGIN_ALLOW_ALL = bool(cors_rule)
print('BASE DIR BASE DIR BASE DIR', BASE_DIR)
TEMPLATES_DIR = os.path.join(BASE_DIR, '/bud_band/templates/')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'budband.wsgi.application'

# REST_FRAMEWORK = {
#     'DEFAULT_RENDERER_CLASSES': (
#         'rest_framework.renderers.JSONRenderer',
#     )
# }

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
}

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

env = environ.Env()
# reading .env file
environ.Env.read_env()

SPOTIFY_CLIENT_ID = env('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = env('SPOTIFY_CLIENT_SECRET')
JWT_SECRET = env('JWT_SECRET')
BUDBAND_PLAYLIST_ID = env('BUDBAND_PLAYLIST_ID')
SPOTIFY_USER_ID = env('SPOTIFY_USER_ID')

# REQUIRED_CONFIG = required_config = {
#     'SPOTIFY_CLIENT_ID': os.environ.get('SPOTIFY_CLIENT_ID'),
#     'SPOTIFY_CLIENT_SECRET': os.environ.get('SPOTIFY_CLIENT_SECRET'),
# }

# SPOTIFY_CLIENT_ID = required_config['SPOTIFY_CLIENT_ID']
# SPOTIFY_CLIENT_SECRET = required_config['SPOTIFY_CLIENT_SECRET']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

POSTGRES_USER = env('POSTGRES_USER')
POSTGRES_PASSWORD = env('POSTGRES_PASSWORD')
POSTGRES_NAME = env('POSTGRES_NAME')
POSTGRES_HOST = env('POSTGRES_HOST')
POSTGRES_PORT = env('POSTGRES_PORT')
POSTGRES_ENGINE = env('POSTGRES_ENGINE')

DATABASES = {
    'default': {
        'ENGINE': POSTGRES_ENGINE,
        'NAME': POSTGRES_NAME,
        'USER': POSTGRES_USER,
        'PASSWORD': POSTGRES_PASSWORD,
        'HOST': POSTGRES_HOST,
        'PORT': POSTGRES_PORT,
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

EDIA_URL = "/mediafiles/"
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")

STATIC_URL = "/staticfiles/"
# STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'bud_band/static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

WEBPACK_STATS = os.path.join(BASE_DIR, 'frontend/webpack-stats.json')
print('webpack states', WEBPACK_STATS)

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'dist/',
        'STATS_FILE': os.path.join(BASE_DIR, 'frontend/webpack-stats.json'),
    }
}
