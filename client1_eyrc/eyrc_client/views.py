import json
from authlib.jose import jwt
from django.dispatch import receiver
from authlib.integrations.django_client import token_update

from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render,redirect
from authlib.integrations.django_client import OAuth

from authlib.oidc.core import CodeIDToken
from authlib.jose import jwt

oauth = OAuth()

oauth.register(
    name = 'eyantra',
    # client_id = "uhmJq6xjFhS9Bu28PILsl4E7",
    # client_secret = "fQvwLfGSHO7uafaJpySK0TGCRcCWD2HPw6MIaWTVVNPuNqnv",
    client_id = "J2FOT0AjSy3OVcdiH7DR10MA",
    client_secret = "D52zZf8NspTTiDhIHgeWuhv6n2A4BuXBw0CirSBYc6aotNMH",
    access_token_url = "https://127.0.0.1:8000/oauth/token/",
    authorize_url = "https://127.0.0.1:8000/oauth/authorize",
    redirect_url = "https://127.0.0.2/authorize",
    grant_type = "authorization_code",
    id_token_signing_alg_values_supported = ['RS256'],
    client_kwargs = {
        'scope':'openid profile',
        'token_endpoint_auth_method': 'client_secret_basic',
    },
    jwks = {
    "keys":   [
                {
                "kty": "RSA",
                "e": "AQAB",
                "use": "sig",
                # "kid": "b16de1b2ab0c16ac0acf662ef01f7567e544252b",
                "alg": "RS256",
                "n": "Lub5dSqbmYujN0L8xhftuV66YeZiai4HoVTG_fjdKEWv7Mpsn3AOIaw0RCs55OJI1PlnBs2ujttvuFQlt8kzNJFpyOOTkbuPrWwxjNlHy44tR42iqiIrt7DUgC5NDseMXl-4t8Psa6QP2NGngvSHu5AiRoTs3UEEVPbtO_Hf6SqtsZJBjUpUUjncUwbMeT2Rp6bff1WblWnNql2lzSJNXldaO9jx4ROcWwHzuSocFvPzwRxz2QRQXhPwKO-DakdXPR4eyhkk7MwrT0ifQjAF09m_3gprWTmtAw9ruMBYkZgyN5IgCkSEME4lY-tdypsdzssmE5rPlXm2TIisJxLPtQs6pv-X_y54ubSUzQaaEY0yMt_EaX2YNIKi-0c5RqWZOWcHvoigOgTgj72M22ffO_-BNOf0ak4qjeDb-fw4OnwApJ3QdsDr2MmVsJFym2rv1gHkbBIQkX51t8zZXYV42-emW3EajqfGe3rC6j48LM7QJzSuStlsMFnyvjU7v1HpwR_BdLg2oLHC9aKBsOuwJCagJIDCX4lFPGob-_uxrDShhBT79GHDM0DGag4at4oJ2oUeQfGvavRcO3Xalc06ECP91dDYF14JjQex3c1z0NEvqSGTXVFgT94YPeXEEjIH5FsXsf7472Pzw9h84ArLCPYGhUhi0Rxrvus"
                }
            ]
    },
    prompt = "select_account"
)


def home(request):
    user = request.session.get('user')
    print('client user: session',user)
    if user:
        user = json.dumps(user)
    return render(request, 'home.html', context={'user': user})


def login(request):
    eyantra = oauth.create_client('eyantra')
    redirect_uri = "https://127.0.0.2:8001/authorize"
    return eyantra.authorize_redirect(request,redirect_uri)                                                   
    #return HttpResponse("login")


def auth(request):
    print('inside callback view in client')
    eyantra = oauth.create_client('eyantra')
    token = eyantra.authorize_access_token(request,verify=False,redirect_uri="https://127.0.0.2:8001/authorize",grant_type="authorization_code")
    print('token is :',token)
    user = eyantra.parse_id_token(request, token)
    print('success________________________________________________')
    print(user)
    request.session['user'] = user.get('name')
    return redirect('/')

def logout(request):
    request.session.pop('user',None)
    return redirect('/')





