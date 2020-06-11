import time

from authlib.oauth2.rfc6749 import (
    TokenMixin,
    AuthorizationCodeMixin,
)
from django.db import models

class OAuth2AuthorizationCodeMixin (AuthorizationCodeMixin):

    code = models.CharField(max_length=120, unique=True, null=False)
    client_id = models.CharField(max_length=48)
    redirect_uri = models.TextField( default='')
    response_type = models.TextField( default='')
    scope = models.TextField( default='')
    nonce = models.TextField()
    auth_time = models.IntegerField(
        null=False,
        default=lambda: int(time.time())
    )

    code_challenge = models.TextField()
    code_challenge_method = models.CharField(max_length=48)

    def is_expired(self):
        return self.auth_time + 300 < time.time()

    def get_redirect_uri(self):
        return self.redirect_uri

    def get_scope(self):
        return self.scope

    def get_auth_time(self):
        return self.auth_time

    def get_nonce(self):
        return self.nonce


class OAuth2TokenMixin(TokenMixin):
    client_id = models.CharField(max_length=48)
    token_type = models.CharField(max_length=40)
    access_token = models.CharField(max_length=255,unique=True, null=False)
    refresh_token = models.CharField(max_length=255, db_index=True)
    scope = models.TextField(default='')
    revoked = models.BooleanField(default=False)
    issued_at = models.IntegerField(
         null=False, default=lambda: int(time.time())
    )
    expires_in = models.IntegerField(null=False, default=0)

    def get_client_id(self):
        return self.client_id

    def get_scope(self):
        return self.scope

    def get_expires_in(self):
        return self.expires_in

    def get_expires_at(self):
        return self.issued_at + self.expires_in