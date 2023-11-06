from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from gestorapp.forms import ConsultationForm
from .models import Consultation, Doctor, Clinic
import datetime
# Create your views here.


def index(request):
    consultations = Consultation.objects.all()
    consultations = consultations.filter(status=True)
    context = {'consultations': consultations}
    return render(request, 'index_consultations.html', context)


def index_doctors(request):
    doctors = Doctor.objects.all()
    doctors = doctors.filter(status=True)
    context = {'docs': doctors}
    return render(request, 'doctors_index.html', context)


def index_clinics(request):
    clinics = Clinic.objects.all()
    clinics = clinics.filter(status=True)
    context = {'clinics': clinics}
    return render(request, 'clincs_index.html', context)


def create(request):
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/consultations')
    else:
        form = ConsultationForm()
    context = {'form': form}
    return render(request, 'create_consultation.html', context)


def update(request, consultation_id):
    consultation = get_object_or_404(Consultation, pk=consultation_id)
    if request.method == 'POST':
        consultation.update_date = datetime.datetime.now()
        form = ConsultationForm(request.POST, instance=consultation)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/consultations')
    else:
        form = ConsultationForm(instance=consultation)
    context = {'form': form}
    return render(request, 'edit_consultation.html', context)


def read(request, consultation_id):
    consultation = get_object_or_404(Consultation, pk=consultation_id)
    context = {'consultation': consultation}
    return render(request, 'detail_consultation.html', context)


def delete(request, consultation_id):
    consultation = get_object_or_404(Consultation, pk=consultation_id)
    if request.method == 'POST':
        consultation.status = False
        consultation.save()
        return HttpResponseRedirect('/consultations')
    context = {'consultation': consultation}
    return render(request, 'delete_consultation.html', context)
