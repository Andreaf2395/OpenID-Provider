#imports

from authlib.oauth2.rfc6749 import grants
from authlib.oidc.core.grants import OpenIDCode
from authlib.common.security import generate_token
from authlib.integrations.django_oauth2 import AuthorizationServer,ResourceProtector,BearerTokenValidator
from .models import OAuth2Client,OAuth2Token,AuthorizationCode
from authlib.integrations.django_oauth2 import RevocationEndpoint
from django.contrib.auth.models import User
from authlib.oidc.core import UserInfo


def read_file(filename):
    with open(filename) as f:
        read_data = f.read()
    print('in read_file')  
    return read_data    


class OpenIDCode(OpenIDCode):
    def exists_nonce(self, nonce, request):
        try:
            AuthorizationCode.objects.get(
                client_id=request.client_id, nonce=nonce
            )
            return True
        except AuthorizationCode.DoesNotExist:
            return False
            

    def get_jwt_config(self, grant):
        return {
            # 'key': 'secret-key',
            'key':  read_file('rsakey'),
            'alg': 'RS256',
            'iss': 'https://127.0.0.1:8000',
            'exp': 3600
        }

    def generate_user_info(self, user, scope):
        user_info = UserInfo(sub=str(user.pk), name=user.username)
        if 'email' in scope:
            user_info['email'] = user.email
        return user_info

class AuthorizationCodeGrant(grants.AuthorizationCodeGrant):
    def create_authorization_code(self, client,grant_user, request):
        code = generate_token(48)
        #open id request has a nonce parameter
        nonce = request.data.get('nonce')

        item = AuthorizationCode(
            code=code,
            client_id=client.client_id,
            redirect_uri=request.data.get('redirect_uri'),
            response_type=request.response_type,
            scope=request.scope,
            user=grant_user,
            nonce=nonce,
        )
        item.save()
        return code

    def parse_authorization_code(self, code, client):
        try:
            item = AuthorizationCode.objects.get(code=code, client_id=client.client_id)
        except AuthorizationCode.DoesNotExist:
            return None

        if not item.is_expired():
            return item

    def delete_authorization_code(self, authorization_code):
        authorization_code.delete()

    def authenticate_user(self, authorization_code):
        print('authorization code user:',authorization_code.user)
        return authorization_code.user

    TOKEN_ENDPOINT_AUTH_METHODS = ['client_secret_basic', 'client_secret_post']


#password grant
class PasswordGrant(grants.ResourceOwnerPasswordCredentialsGrant):
    def authenticate_user(self, username, password):
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None


#refresh token grant
class RefreshTokenGrant(grants.RefreshTokenGrant):
    def authenticate_refresh_token(self, refresh_token):
        try:
            item = OAuth2Token.objects.get(refresh_token=refresh_token)
            if item.is_refresh_token_active():
                return item
        except OAuth2Token.DoesNotExist:
            return None

    def authenticate_user(self, credential):
        return credential.user

    def revoke_old_credential(self, credential):
        credential.revoked = True
        credential.save()

#auth server

server = AuthorizationServer(OAuth2Client, OAuth2Token)

#require oauth
require_oauth = ResourceProtector()
server.register_grant(AuthorizationCodeGrant, [OpenIDCode(require_nonce=True)])
server.register_endpoint(RevocationEndpoint)
require_oauth.register_token_validator(BearerTokenValidator(OAuth2Token))




@require_oauth('profile')
def user_profile(request):
    user = request.oauth_token.user
    return JsonResponse(dict(sub=user.pk, username=user.username))



#config oauth
def config_oauth(app):
    server.init_app(app)

    #server.register_grant(PasswordGrant)
    #server.register_grant(RefreshTokenGrant)


