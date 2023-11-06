from django.contrib import admin
from .models import Doctor, Clinic, Consultation

# Register your models here.


class DoctorAdmin(admin.ModelAdmin):
    list_display = ["fullname", "phone_number",
                    "create_date", "update_date", "status"]


class ClinicAdmin(admin.ModelAdmin):
    list_display = ["name", "adress", "create_date", "update_date", "status"]


class ConsultationAdmin(admin.ModelAdmin):
    list_display = ["service", "price", "doctor",
                    "animal", "create_date", "update_date", "status"]


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Clinic, ClinicAdmin)
admin.site.register(Consultation, ConsultationAdmin)
