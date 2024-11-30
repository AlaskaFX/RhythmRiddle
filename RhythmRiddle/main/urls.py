
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('/puzzle', views.puzzle, name='puzzle'), # Пазлы

    path('/search', views.search, name='search'), # Поиск
    path('/get_quiz', views.get_quiz, name='get_quiz'), # Выбор задания
    path('/update_stats', views.update_user_stats, name='update_stats'), # Обновление статистики пользователя

    path('', views.feed, name='feed'), # Главное
    path('/increment_play_count/<int:song_id>/', views.increment_play_count, name='increment_play_count'), # Обновление счетчика прослушивании
    path('/update-genres/', views.update_genres, name='update_genres'), # Обновление предпочтений пользователя

    path('/playlists', views.playlists, name='playlists'), # Плейлисты
    path('/create_playlist', views.create_playlist, name='create_playlist'), # Создание плейлиста
    path('/playlists/<int:id>/', views.playlist_detail, name='playlist_detail'), # Содержание плейлиста

    path('/subscription', views.subscription, name='subscription'), # Подписка

    path('/data', views.data, name='account_data'), # Профиль
    path('/card', views.card, name='account_card'), # Данные карты

    path('/favorites', views.favorites, name='favorites'), # Избранные
    path('/add_favorite/<int:song_id>/', views.add_favorite, name='add_favorite'), # Добавление в избранные

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)