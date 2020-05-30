from django.contrib import admin
from .models import ORMNews, ORMAudience

class ORMNewsAdmin(admin.ModelAdmin):
    list_display = ('news_title', 'publish_date')
    search_fields = ('news_title','publish_date')
    filter_horizontal = ('audience',)

#class ORMAudienceAdmin(admin.ModelAdmin)

admin.site.register(ORMNews, ORMNewsAdmin)
admin.site.register(ORMAudience)
