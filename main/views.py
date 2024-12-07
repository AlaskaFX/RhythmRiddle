
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Song, Stats, Quiz, FavoriteSong, Playlist
from .forms import PlaylistForm
import random, json

@login_required
def puzzle(request):
    user_stats = Stats.objects.get(user=request.user)
    return render(request, 'main/puzzle.html', {"user_stats": user_stats})

def get_quiz(request):
    if request.method == 'GET':
        quiz_type = request.GET.get('type')
        difficulty = request.GET.get('difficulty')

        quizzes = Quiz.objects.filter(quiz_type=quiz_type, difficulty=difficulty)
        if quizzes.exists():
            quiz = random.choice(quizzes)
            response_data = {
                'correct_answer': quiz.correct_answer,
                'wrong_answers': [
                    quiz.wrong_answer1,
                    quiz.wrong_answer2,
                    quiz.wrong_answer3,
                ],
                'song_file': quiz.song_file.url,
            }
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Нет заданий по этому типу и сложности.'}, status=404)

@login_required
@require_POST
def update_user_stats(request):
    stats = Stats.objects.get(user=request.user)

    if stats.attempts > 0:
        stats.attempts -= 1

    result = request.POST.get('result')
    if result == 'win':
        stats.points += 10
    elif result == 'lose':
        stats.points -= 10

    if stats.points < 0:
        stats.points = 0

    stats.save()

    return JsonResponse({
        'success': True,
        'points': stats.points,
        'attempts': stats.attempts,
    })

def search(request):
    query = request.GET.get('q', '')
    genre_filter = request.GET.get('genre', '')
    artist_filter = request.GET.get('artist', '')

    songs = Song.objects.all()

    if query:
        songs = songs.filter(title__icontains=query) | songs.filter(artist__icontains=query)

    if genre_filter:
        songs = songs.filter(song_genre=genre_filter)

    if artist_filter:
        songs = songs.filter(artist__icontains=artist_filter)

    unique_genres = Song.objects.values_list('song_genre', flat=True).distinct()
    genre_dict = dict(Song.SONG_GENRE)
    filtered_genres = {genre: genre_dict[genre] for genre in unique_genres if genre in genre_dict}

    unique_artists = Song.objects.values_list('artist', flat=True).distinct()

    return render(request, 'main/search.html', {
        'songs': songs,
        'query': query,
        'unique_genres': filtered_genres,
        'unique_artists': unique_artists,
    })

@login_required
def feed(request):
    stats = Stats.objects.get(user=request.user)

    user_genres = [stats.first_user_genre, stats.second_user_genre, stats.third_user_genre]
    user_genres = [genre for genre in user_genres if genre]

    if user_genres:
        filtered_songs = list(Song.objects.filter(song_genre__in=user_genres))
        quick_picks = random.sample(filtered_songs, min(len(filtered_songs), 4))
    else:
        quick_picks = []

    songs = list(Song.objects.all())
    user_playlists = Playlist.objects.filter(owner=request.user)
    shared_playlists = Playlist.objects.exclude(owner=request.user)

    if not songs:
        random_songs = []
        top_song = None
    else:
        random_songs = random.sample(songs, min(len(songs), 4))
        top_song = Song.objects.order_by('-play_count').first()

    context = {
        'track': random_songs[0] if random_songs else None,
        'quick_picks': quick_picks,
        'song': top_song,
        'stats': stats,
        'user_playlists': user_playlists,
        'shared_playlists': shared_playlists,
    }

    return render(request, 'main/feed.html', context)

def increment_play_count(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    song.play_count += 1
    song.save()

    return JsonResponse({'play_count': song.play_count})

@login_required
@require_POST
def update_genres(request):
    data = json.loads(request.body)
    genres = data.get('genres', [])

    stats = Stats.objects.get(user=request.user)

    if genres:
        for i, genre in enumerate(genres):
            if i == 0:
                stats.first_user_genre = genre
            elif i == 1:
                stats.second_user_genre = genre
            elif i == 2:
                stats.third_user_genre = genre
    else:
        stats.first_user_genre = None
        stats.second_user_genre = None
        stats.third_user_genre = None

    stats.save()
    return JsonResponse({'status': 'success'})

@login_required
def playlists(request):
    my_playlists = Playlist.objects.filter(owner=request.user)
    shared_playlists = Playlist.objects.exclude(owner=request.user)

    return render(request, 'main/playlists.html', {
        'my_playlists': my_playlists,
        'shared_playlists': shared_playlists,
    })

@login_required
def create_playlist(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST, request.FILES)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.owner = request.user
            playlist.save()
            return redirect('playlists')
        else:
            print(form.errors)
    else:
        form = PlaylistForm()

    return render(request, 'main/create_playlist.html', {'form': form})

@login_required
def playlist_detail(request, id):
    playlist = get_object_or_404(Playlist, id=id)

    songs = playlist.songs.all()

    return render(request, 'main/playlist_detail.html', {
        'playlist': playlist,
        'songs': songs,
    })

@login_required
def add_favorite(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    FavoriteSong.objects.get_or_create(user=request.user, song=song)

    next_url = request.META.get('HTTP_REFERER', 'feed')
    return redirect(next_url)

def subscription(request):
    return render(request, 'main/subscription.html')

@login_required
def favorites(request):
    favorite_songs = FavoriteSong.objects.filter(user=request.user).select_related('song')
    return render(request, 'main/favorites.html', {'favorite_songs': favorite_songs})

###

@login_required
def data(request):
    return render(request, 'main/account_data.html')

@login_required
def card(request):
    return render(request, 'main/account_card.html')
