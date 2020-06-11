from django.contrib import admin
from .models import OAuth2Client,AuthorizationCode,OAuth2Token
class Oauth2ClientAdmin(admin.ModelAdmin):
    pass
class Oauth2TokenAdmin(admin.ModelAdmin):
    pass
class AuthorizationCodeAdmin(admin.ModelAdmin):
    pass

admin.site. register ( OAuth2Client,Oauth2ClientAdmin)
admin.site.register(AuthorizationCode,AuthorizationCodeAdmin)
admin.site.register(OAuth2Token,Oauth2TokenAdmin)
