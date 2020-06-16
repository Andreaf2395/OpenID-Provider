import json
from authlib.jose import jwt
from django.dispatch import receiver
from authlib.integrations.django_client import token_update

from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render,redirect
from authlib.integrations.django_client import OAuth
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
    client_kwargs = {
        'scope':'openid profile',
        'token_endpoint_auth_method': 'client_secret_basic',
    },
    prompt = "select_account"
)


def home(request):
    user = request.session.get('current_user')
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
    print(type(token))
    user = eyantra.parse_id_token(request, token)
    print('success________________________________________________')
    print(user)
    request.session['user'] = user
    return redirect('/')

def logout(request):
    request.session.pop('user',None)
    return redirect('/')





