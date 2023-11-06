from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from webapp.forms import AnimalForm
from .models import Animal, AnimalDetail
import datetime
# Create your views here.


def index(request):
    animals = Animal.objects.all()
    animals = animals.filter(status=True)
    context = {'animals': animals}
    return render(request, 'index_animals.html', context)


def animals_details(request):
    animals_details = AnimalDetail.objects.all()
    animals_details = animals_details.filter(status=True)
    context = {'animals': animals_details}
    return render(request, 'animaldetail_index.html', context)


def create(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/animals')
    else:
        form = AnimalForm()
    context = {'form': form}
    return render(request, 'create_animal.html', context)


def update(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    if request.method == 'POST':
        animal.update_date = datetime.datetime.now()
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/animals')
    else:
        form = AnimalForm(instance=animal)
    context = {'form': form}
    return render(request, 'edit_animal.html', context)


def read(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    context = {'animal': animal}
    return render(request, 'detail_animal.html', context)


def delete(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    if request.method == 'POST':
        animal.status = False
        animal.save()
        return HttpResponseRedirect('/animals')
    context = {'animal': animal}
    return render(request, 'delete_animal.html', context)
