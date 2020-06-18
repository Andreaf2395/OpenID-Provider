import time
from django.contrib import auth
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from authlib.oauth2 import OAuth2Error
from django.http import JsonResponse
from .models import User,OAuth2Client
from .oauth2 import server,require_oauth
from authlib.common.security import generate_token
from authlib.integrations.django_oauth2 import RevocationEndpoint
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required



def current_user(request):
    if 'id' in request.session:
        uid = request.session['id']
        return User.objects.get(id=uid)
    return None
def home(request):
    if request.method == "POST":
        username = request.POST["username"]
        user = User.objects.filter(username=username)[0]
        if not user:
            user = User(username=username)
            user.save()
        request.session['id'] = user.id
        return redirect('/')
    user = current_user(request)
    if user:
        clients = OAuth2Client.objects.filter(user=user.id)
        print(user,clients)
    else:
        clients = []
    context = {'user':user,'clients':clients}
    return render(request,'home.html',context)


def split_by_crlf(s):
    return [v for v in s.splitlines() if v]

def create_client(request):
    if not request.user:
        return redirect('/')
    if request.method == 'GET':
        return render(request,'create_client.html')
    client_id = generate_token(24)
    client = OAuth2Client(client_id=client_id,user=request.user)

    if client.token_endpoint_auth_method == 'None':
        client.client_secret = ''
    else:
        client.client_secret = generate_token(48)
    client_metadata = {
        "client_name" : request.POST["client_name"],
        #"client_uri" : request.POST["client_uri"],
        "grant_types": split_by_crlf(request.POST["grant_type"]),
        "redirect_uris": split_by_crlf(request.POST["redirect_uri"]),
        "response_types": split_by_crlf(request.POST["response_type"]),
        "scope": request.POST["scope"],
        "token_endpoint_auth_method": request.POST["token_endpoint_auth_method"]

    }
    #client.set_client_metadata(client_metadata)
    client.client_name = client_metadata["client_name"]
    client.grant_type = client_metadata["grant_types"]
    client.redirect_uris = client_metadata["redirect_uris"]
    client.response_type = client_metadata["response_types"]
    client.scope = client_metadata["scope"]
    client.token_endpoint_auth_method = client_metadata["token_endpoint_auth_method"]
    client.save()
    return redirect('/')



def authorize(request):
    
    user = request.user
    print('user:',user)
    if not user or request.user.is_anonymous:
        return redirect('oauth_login')
    if request.method == 'GET':
        try:
            #print(request)
            grant = server.validate_consent_request(request,end_user=user)
            print('grant is :',grant)
            context = dict(grant=grant, user=request.user)

        except OAuth2Error as error:
            print('error')
            return JsonResponse(dict(error.get_body()))

        return render(request, 'authorize.html', context)

    confirmed = request.POST['confirm']
    if confirmed:
        # granted by resource owner
        print('user_confirmed authorization')
        return server.create_authorization_response(request, grant_user=request.user)

    # denied by resource owner
    print('out here')
    return server.create_authorization_response(request, grant_user=None)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        print('isnide provider login',user)
        if user is not None and  user is not 'AnonymousUser':
            auth.login(request, user)

            print('finally going ...')
            return redirect('')
        else:

            return redirect(request,'oauth_login')
    else:
        return render(request, 'sign-in_temp.html')

# use ``server.create_token_response`` to handle token endpoint

@csrf_exempt
@require_http_methods(["POST"])  # we only allow POST for token endpoint
def issue_token(request):
    print('inside issue token2')
    print(request.headers)
    print(request.body)
    val = server.create_token_response(request)
    print('token resp:',val)
    return val

@require_http_methods(["POST"])
def revoke_token(request):
    return server.create_endpoint_response(RevocationEndpoint.ENDPOINT_NAME, request)

@require_oauth('profile')
def user_profile(request):
    user = request.oauth_token.user
    return JsonResponse(dict(sub=user.pk, username=user.username))
