from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from players.forms import PlayerForm
from .models import Player


def index(request):
    players = Player.objects.all()
    return render(request, 'index_players.html', {'players': players})


def create(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/players')
    else:
        form = PlayerForm()
    return render(request, 'create_player.html', {'form': form})


def detail(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    return render(request, 'detail_player.html', {'player': player})


def edit(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/players')
    else:
        form = PlayerForm(instance=player)
    return render(request, 'edit_player.html', {'form': form})


def delete(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    if request.method == 'POST':
        player.delete()
        return HttpResponseRedirect('/players')
    return render(request, 'delete_player.html', {'player': player})
