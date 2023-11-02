from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from leagues.forms import LeagueForm
from .models import League


def index(request):
    leagues = League.objects.all()
    return render(request, 'index_leagues.html', {'leagues': leagues})


def create(request):
    if request.method == 'POST':
        form = LeagueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/leagues')
    else:
        form = LeagueForm()
    return render(request, 'create.html', {'form': form})


def detail(request, league_id):
    league = get_object_or_404(League, pk=league_id)
    return render(request, 'detail.html', {'league': league})


def edit(request, league_id):
    league = get_object_or_404(League, pk=league_id)
    if request.method == 'POST':
        form = LeagueForm(request.POST, instance=league)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/leagues')
    else:
        form = LeagueForm(instance=league)
    return render(request, 'edit.html', {'form': form})


def delete(request, league_id):
    league = get_object_or_404(League, pk=league_id)
    if request.method == 'POST':
        league.delete()
        return HttpResponseRedirect('/leagues')
    return render(request, 'delete.html', {'league': league})
