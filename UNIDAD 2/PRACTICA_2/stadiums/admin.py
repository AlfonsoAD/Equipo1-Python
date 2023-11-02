from django.contrib import admin
from .models import Stadium


class StadiumAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'capacity', 'team')


admin.site.register(Stadium, StadiumAdmin)
