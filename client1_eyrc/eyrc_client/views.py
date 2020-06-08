import json

from django.urls import reverse
from django.shortcuts import render,redirect
from django.dispatch import receiver
from authlib.integrations.django_client import token_update
from authlib.integrations.django_client import OAuth

oauth = OAuth()

oauth.register(
    name = 'eyantra',
    access_token_url = "https://127.0.0.1:8000/oauth/token",
    authorize_url = "https://127.0.0.1:8000/oauth/authorize",
    client_kwargs = {
        'scope':'openid email profile'
    }
)

def home(request):
    user = request.session.get('user')
    if user:
        user = json.dumps(user)
    return render(request,'home.html',context= {'user':user})

def login(request):
    print('login me..')
    #redirect_uri = request.build_absolute_uri(reverse('authorize'))
    #print(redirect_uri)
    redirect_uri = "https://127.0.0.2:8001/authorize"
    return oauth.eyantra.authorize_redirect(request,redirect_uri)

def auth(request):
    print('inside auth view')
    token = oauth.eyantra.authorize_access_token(request)
    user = oauth.eyantra.parse_id_token(request,token)
    request.session['user'] = user
    return redirect('/')

def logout(request):
    request.session.pop('user',None)
    return redirect('/')



