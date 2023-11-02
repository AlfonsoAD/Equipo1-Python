from django.contrib import admin
from .models import League


class LeaguesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country')


admin.site.register(League, LeaguesAdmin)
