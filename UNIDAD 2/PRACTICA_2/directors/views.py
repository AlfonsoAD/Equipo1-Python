from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Technical_Director
from directors.forms import DirectorForm


def index(request):
    directors = Technical_Director.objects.all()
    return render(request, 'index_directors.html', {'directors': directors})


def detail(request, director_id):
    director = get_object_or_404(Technical_Director, pk=director_id)
    return render(request, 'detail_director.html', {'director': director})


def create(request):
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/directors')
    else:
        form = DirectorForm()
    return render(request, 'create_director.html', {'form': form})


def edit(request, director_id):
    director = get_object_or_404(Technical_Director, pk=director_id)
    if request.method == 'POST':
        form = DirectorForm(request.POST, instance=director)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/directors')
    else:
        form = DirectorForm(instance=director)
    return render(request, 'edit_director.html', {'form': form})


def delete(request, director_id):
    director = get_object_or_404(Technical_Director, pk=director_id)
    if request.method == 'POST':
        director.delete()
        return HttpResponseRedirect('/directors')
    return render(request, 'delete_director.html', {'director': director})
