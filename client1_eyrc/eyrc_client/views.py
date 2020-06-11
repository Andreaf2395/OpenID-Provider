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
    client_id = "uhmJq6xjFhS9Bu28PILsl4E7",
    client_secret = "fQvwLfGSHO7uafaJpySK0TGCRcCWD2HPw6MIaWTVVNPuNqnv",
    access_token_url = "https://127.0.0.1:8000/oauth/token/",
    authorize_url = "https://127.0.0.1:8000/oauth/authorize",
    redirect_url = "https://127.0.0.2/authorize",
    grant_type = "authorization_code",
    client_kwargs = {
        'scope':'openid email profile',

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
    print('inside callback')
    eyantra = oauth.create_client('eyantra')
    token = eyantra.authorize_access_token(request,verify=False,client_id = "uhmJq6xjFhS9Bu28PILsl4E7",client_secret="fQvwLfGSHO7uafaJpySK0TGCRcCWD2HPw6MIaWTVVNPuNqnv")
    print('token is :',token)
    user = eyantra.parse_id_token(request, json.loads(token))
    request.session['user'] = user
    return redirect('/')

def logout(request):
    request.session.pop('user',None)
    return redirect('/')





