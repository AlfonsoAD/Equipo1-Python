from django.contrib import admin
from .models import Player


class PlayersAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'age',
                    'position', 'shirt_number', 'country')


admin.site.register(Player, PlayersAdmin)
