
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .models import Song
import random


@login_required
def puzzle(request):
    return render(request, 'main/puzzle.html')

def search(request):
    return render(request, 'main/search.html')

def feed(request):
    songs = list(Song.objects.all())
    random_songs = random.sample(songs, min(len(songs), 4))

    context = {
        'track': random_songs[0] if random_songs else None,
        'quick_picks': random_songs,
    }

    return render(request, 'main/feed.html', context)

@login_required
def playlists(request):
    return render(request, 'main/playlists.html')


def subscription(request):
    return render(request, 'main/subscription.html')

###

@login_required
def data(request):
    return render(request, 'main/account_data.html')

@login_required
def card(request):
    return render(request, 'main/account_card.html')