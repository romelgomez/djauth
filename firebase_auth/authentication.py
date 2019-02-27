import os
import base64
import datetime
import random
import time
import uuid
import six

import pytest
import requests

import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials

# import google.oauth2.credentials
# from google.auth import transport

_verify_token_url = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyCustomToken'
_verify_password_url = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword'
_password_reset_url = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/resetPassword'
_verify_email_url = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/setAccountInfo'
_email_sign_in_url = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/emailLinkSignin'

from django.conf import settings
from django.contrib.auth.models import User

from rest_framework.exceptions import APIException
from rest_framework import status, authentication, exceptions
from rest_framework.permissions import IsAuthenticated

# json = os.path.join(os.getcwd(), 'firebase_auth/fire_key.json')
# cred = credentials.Certificate(json)
# default_app = firebase_admin.initialize_app(cred)

# userData = auth.get_user_by_email('')

# print ('[dict] user custom_claims  >>>', userData.custom_claims)
# print ('[bool] user.disabled  >>>', userData.disabled)
# print ('[bool] user.email_verified  >>>', userData.email_verified)
# print ('[list] user.provider_data   >>>', userData.provider_data)
# print ('[string] user.display_name >>>', userData.display_name)
# print ('[string] user.email  >>>', userData.email)
# print ('[string] user.phone_number >>>', userData.phone_number)
# print ('[string] user.photo_url >>>', userData.photo_url)
# print ('[string] user.provider_id >>>', userData.provider_id)
# print ('[string] user.tokens_valid_after_timestamp >>>', userData.tokens_valid_after_timestamp)
# print ('[string] user.uid >>>', )
# print ('[string] user.user_metadata.creation_timestamp >>>', userData.user_metadata.creation_timestamp)
# print ('[string] user.user_metadata.last_sign_in_timestamp   >>>', userData.user_metadata.last_sign_in_timestamp)


class FirebaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        id_token = request.META.get('HTTP_AUTHORIZATION')

        print('id_token >>>', id_token)

        decoded_token = None
        try:
            decoded_token = auth.verify_id_token(id_token)
        except Exception as e:
            pass

        if not id_token or not decoded_token:
            return None

        uid = decoded_token.get('uid')
        try:
            user = User.objects.get(username=uid)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('The user does not exist')

        return (user, None)

# >>>> Exceptions <<<<
class NoAuthToken(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = 'No authentication token provided'
    default_code = 'no_auth_token'

class InvalidAuthToken(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = 'Invalid authentication token provided'
    default_code = 'invalid_token'

class FirebaseError(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'The user provided with the auth token is not a valid Firebase user, it has no Firebase UID'
    default_code = 'no_firebase_uid'


# >>>> Mixins <<<<<
class FirebaseAuthMixin():
    permission_classes = (IsAuthenticated,)
    authentication_classes = (FirebaseAuthentication,)


# additional_claims = {
#   "premiumAccount": True
# }

# API_KEY = ''

# def _sign_in(custom_token, api_key):
#   # The api_key is the public key
#     body = {'token' : custom_token.decode("utf-8"), 'returnSecureToken' : True}
#     params = {'key' : api_key}
#     resp = requests.request('post', _verify_token_url, params=params, json=body)
#     resp.raise_for_status()
#     return resp.json().get('idToken')

# def test_custom_token():
#     # custom_token = auth.create_custom_token(userData.uid, additional_claims)
#     custom_token = auth.create_custom_token(userData.uid)
#     id_token = _sign_in(custom_token, API_KEY)
#     claims = auth.verify_id_token(id_token)
    
#     print(claims)
#     # {'iss': 'https://securetoken.google.com/<app_name>', 'aud': '<app_name>', 'auth_time': 1550759505, 'user_id': '555000444', 'sub': '555000444', 'iat': 1550759505, 'exp': 1550763105, 'email': '', 'email_verified': True, 'firebase': {'identities': {'email': ['']}, 'sign_in_provider': 'custom'}, 'uid': '555000444'}

#     assert claims['uid'] == userData.uid
