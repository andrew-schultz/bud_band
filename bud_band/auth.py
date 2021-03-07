import base64
import os
import time
import uuid
from binascii import hexlify

import jwt
from django.contrib.auth.models import AnonymousUser, User
from django.db.models import Q
from django.utils import timezone
from rest_framework import exceptions
from rest_framework.authentication import (BaseAuthentication,
                                           get_authorization_header)

from bud_band.error import ExpiredToken, InvalidToken, MissingToken

class JWTAuthentication(BaseAuthentication):
    model = None

    def get_model(self):
        return User

    def authenticate_header(self, request):
        return 'Bearer'

    def authenticate(self, request):
        auth = get_authorization_header(request).split()
        if not auth:
            raise MissingToken("Auth token is a required field")

        if len(auth) != 2:
            raise InvalidToken("Invalid auth header")

        bearer, token = auth
        if bearer != b'Bearer':
            raise InvalidToken("Bearer is a required field")

        # get jwt secret from env var
        jwt_secret = None
        try:
            jwt_secret = os.environ['JWT_SECRET']
        except KeyError:
            raise InvalidToken("JWT_SECRET not defined")

        # decode the token
        try:
            payload = jwt.decode(token.decode('utf8'), jwt_secret, algorithm='HS256')
        except jwt.ExpiredSignatureError:
            raise ExpiredToken("Signature expired")
        except jwt.exceptions.DecodeError:
            raise InvalidToken("Decode error")
        except jwt.InvalidTokenError:
            raise InvalidToken("Invalid token")

        # user should always be encoded in token
        user = payload.get('user', None)
        if user is None:
            raise InvalidToken("Invalid payload")

        # get user uuid and decode
        uuid_value = user.get('uuid', None)

        try:
            uuid.UUID(uuid_value)
        except ValueError:
            uuid_value = hexlify(base64.urlsafe_b64decode(uuid_value + '==')).decode()

        # make sure user is valid
        user = None
        try:
            user = User.objects.get(profile__uuid=uuid_value)
        except User.DoesNotExist:
            raise InvalidToken("Invalid user associated with jwt")

        return (user, token)



class AppUser(AnonymousUser):
    """ Django authentication requires a returned user. SignatureAuthentication will return an
    instance of this class"""
    is_authenticated = False

    def __init__(self, is_authenticated=False):
        self.is_authenticated = is_authenticated

    def get_username():
        return 'app_user'
