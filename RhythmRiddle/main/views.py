
from django.shortcuts import render
from django.http import HttpResponse

def puzzle(request):
    return render(request, 'main/puzzle.html')

def search(request):
    return render(request, 'main/search.html')

def feed(request):
    return render(request, 'main/feed.html')

def playlists(request):
    return render(request, 'main/playlists.html')

def subscription(request):
    return render(request, 'main/subscription.html')

###

def data(request):
    return render(request, 'main/account_data.html')

def card(request):
    return render(request, 'main/account_card.html')