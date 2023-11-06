from django.contrib import admin
from .models import Animal, AnimalDetail

# Register your models here.


class AnimalAdmin(admin.ModelAdmin):
    list_display = ["name", "race",
                    "admission_date", "departure_date", "status"]


class AnimalDetailAdmin(admin.ModelAdmin):
    list_display = ["weight", "color", "animal", "status"]


admin.site.register(Animal, AnimalAdmin)
admin.site.register(AnimalDetail, AnimalDetailAdmin)
