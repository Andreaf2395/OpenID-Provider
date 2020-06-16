import time
from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE
from authlib.oauth2.rfc6749 import AuthorizationCodeMixin,ClientMixin,TokenMixin
from authlib.oauth2.rfc6749.util import scope_to_list,list_to_scope
from authlib.oidc.core import grants, UserInfo
from django.utils.functional import cached_property
from .client_mixin import OAuth2ClientMixin
from .token_mixin import OAuth2AuthorizationCodeMixin,OAuth2TokenMixin
from authlib.common.encoding import json_loads, json_dumps

class OAuth2Client( models.Model , ClientMixin):
    user = models.ForeignKey(User, on_delete=CASCADE)
    client_id = models.CharField(max_length=48, unique=True, db_index=True)
    client_secret = models.CharField(max_length=48, blank=True)
    client_name = models.CharField(max_length=120)
    redirect_uris = models.TextField(default='')
    default_redirect_uri = models.TextField(blank=False, default='')
    scope = models.TextField(default='')
    response_type = models.TextField(default='')
    grant_type = models.TextField(default='')
    token_endpoint_auth_method = models.CharField(max_length=120, default='')

    # you can add more fields according to your own need
    # check https://tools.ietf.org/html/rfc7591#section-2

    def set_client_metadata(self, value):
        self._client_metadata = json_dumps(value)

    def get_client_id(self):
        print('self.client id:',self.client_id)
        return self.client_id

    def get_default_redirect_uri(self):
        return self.default_redirect_uri

    def get_allowed_scope(self, scope):
        if not scope:
            return ''
        allowed = set(scope_to_list(self.scope))
        return list_to_scope([s for s in scope.split() if s in allowed])

    def check_redirect_uri(self, redirect_uri):

        if redirect_uri == self.default_redirect_uri:
            print('redirect is true')
            return True
        return redirect_uri in self.redirect_uris

    def has_client_secret(self):
        print('secret:', self.client_secret)
        return bool(self.client_secret)

    def check_client_secret(self, client_secret):
        if self.client_secret==client_secret:
            print('client_secret is correct')
        else:
            print('client secret is not correct')
        return self.client_secret == client_secret

    def check_token_endpoint_auth_method(self, method):
        if self.token_endpoint_auth_method == method:
            print('token auth method is True')
        else:
            print('token auth method is false')
        return self.token_endpoint_auth_method == method

    def check_response_type(self, response_type):
        if response_type in self.response_type:
            print('yes response type is in allowwed')
        else:
            print('no response type is not in allowwed')
        #print('response type:',type(response_type))
        #print('self.response type:',type(self.response_type))
        #allowed = self.response_type.split()
        #print('allowed:',allowed)
        return response_type in self.response_type

    def check_grant_type(self, grant_type):
        print('grant type:',grant_type)
        allowed = self.grant_type
        print('DB grant type:',allowed)
        if grant_type in allowed:
            print('yes grant type is in allowed')
        else:
            print('grant type is not allowed')
        return grant_type in allowed

def now_timestamp():
    return int(time.time())

class AuthorizationCode(models.Model, AuthorizationCodeMixin):
    user = models.ForeignKey(User, on_delete=CASCADE)
    client_id = models.CharField(max_length=48, db_index=True)
    code = models.CharField(max_length=120, unique=True, null=False)
    redirect_uri = models.TextField(default='', null=True)
    response_type = models.TextField(default='')
    scope = models.TextField(default='', null=True)
    auth_time = models.IntegerField(null=False, default=now_timestamp)
    nonce = models.CharField(max_length=120,default='',null=True)

    def is_expired(self):
        return self.auth_time + 300 < time.time()

    def get_redirect_uri(self):
        return self.redirect_uri

    def get_scope(self):
        return self.scope or ''

    def get_auth_time(self):
        return self.auth_time

    def get_nonce(self):
        return self.nonce;    
  

class OAuth2Token(models.Model, TokenMixin):
    user = models.ForeignKey(User, on_delete=CASCADE)
    client_id = models.CharField(max_length=48, db_index=True)
    token_type = models.CharField(max_length=40)
    access_token = models.CharField(max_length=255, unique=True, null=False)
    refresh_token = models.CharField(max_length=255, db_index=True)
    scope = models.TextField(default='')
    revoked = models.BooleanField(default=False)
    issued_at = models.IntegerField(null=False, default=now_timestamp)
    expires_in = models.IntegerField(null=False, default=0)

    def get_client_id(self):
        return self.client_id

    def get_scope(self):
        return self.scope

    def get_expires_in(self):
        return self.expires_in

    def get_expires_at(self):
        return self.issued_at + self.expires_in

    def is_refresh_token_active(self):
        if self.revoked:
            return False
        expires_at = self.issued_at + self.expires_in * 2
        return expires_at >= time.time()