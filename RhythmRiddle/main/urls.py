
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
    path('/playlists', views.playlists, name='playlists'), # Плейлисты
    path('/subscription', views.subscription, name='subscription'), # Подписка

    path('/data', views.data, name='account_data'), # Профиль
    path('/card', views.card, name='account_card'), # Данные карты

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)