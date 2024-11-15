
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from yandex_music import Client

client = Client('token').init()

@login_required
def puzzle(request):
    return render(request, 'main/puzzle.html')

@login_required
def search(request):
    return render(request, 'main/search.html')

@login_required
def feed(request):
    # track_list = client.tracks(['32881882:4009574']) # Мой номер 245
    track_list = client.tracks(['25996081:11277'])  # Владимирский централ
    track_info = {
        'title': track_list[0].title,
        'artists': ', '.join(artist.name for artist in track_list[0].artists),
        # 'duration': f"{track_list[0].duration_ms // 60000}:{(track_list[0].duration_ms // 1000) % 60:02d}",
        'track_id': track_list[0],
        'cover': track_list[0].cover_uri.replace('%%', '200x200')
    }
    return render(request, 'main/feed.html', {'track': track_info})

@login_required
def download_music(request):
    track_list = client.tracks(['25996081:11277'])
    track_to_download = track_list[0]

    file_path = f"{track_to_download.title}.mp3"
    track_to_download.download(file_path)

    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='audio/mpeg')
        response['Content-Disposition'] = f'attachment; filename="{track_to_download.title}.mp3"'
        return response

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