
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

@login_required
def puzzle(request):
    return render(request, 'main/puzzle.html')

@login_required
def search(request):
    return render(request, 'main/search.html')

@login_required
def feed(request):
    return render(request, 'main/feed.html')

@login_required
def playlists(request):
    return render(request, 'main/playlists.html')

@login_required
def subscription(request):
    return render(request, 'main/subscription.html')

###

@login_required
def data(request):
    return render(request, 'main/account_data.html')

@login_required
def card(request):
    return render(request, 'main/account_card.html')