from django.contrib import admin
from .models import Team


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'league', 'count_players', 'technical_director')


admin.site.register(Team, TeamAdmin)
