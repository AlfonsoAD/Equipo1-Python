from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from teams.forms import TeamForm
from .models import Team


def index(request):
    teams = Team.objects.all()
    return render(request, 'index_teams.html', {'teams': teams})


def create(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teams')
    else:
        form = TeamForm()
    return render(request, 'create_team.html', {'form': form})


def detail(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    return render(request, 'detail_team.html', {'team': team})


def edit(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teams')
    else:
        form = TeamForm(instance=team)
    return render(request, 'edit_team.html', {'form': form})


def delete(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    if request.method == 'POST':
        team.delete()
        return HttpResponseRedirect('/teams')
    return render(request, 'delete_team.html', {'team': team})
