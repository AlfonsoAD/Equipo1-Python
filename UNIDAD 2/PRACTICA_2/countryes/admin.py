from django.contrib import admin
from .models import Country


class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Country, CountryAdmin)
