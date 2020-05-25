from django.contrib import admin
from .models import ORMInitiative

class InitiativeAdmin(admin.ModelAdmin):
    list_display = ('acronym', 'full_name')
    search_fields = ('acronym', 'full_name')

admin.site.register(ORMInitiative, InitiativeAdmin)