
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.shortcuts import render
from .models import Song, Stats, Quiz
import random

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

    # Фильтрация песен по запросу
    songs = Song.objects.all()

    if query:
        songs = songs.filter(title__icontains=query) | songs.filter(artist__icontains=query)

    if genre_filter:
        songs = songs.filter(song_genre=genre_filter)

    if artist_filter:
        songs = songs.filter(artist__icontains=artist_filter)

    # Получаем уникальные жанры и исполнителей
    unique_genres = Song.objects.values_list('song_genre', flat=True).distinct()
    unique_artists = Song.objects.values_list('artist', flat=True).distinct()

    return render(request, 'main/search.html', {
        'songs': songs,
        'query': query,
        'unique_genres': unique_genres,
        'unique_artists': unique_artists,
    })

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
