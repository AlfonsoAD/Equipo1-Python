from django.contrib import admin
from .models import Technical_Director


class DirectorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')


admin.site.register(Technical_Director, DirectorsAdmin)
