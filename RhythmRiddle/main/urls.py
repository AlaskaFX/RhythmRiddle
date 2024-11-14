
from django.urls import path
from . import views

urlpatterns = [
    path('/puzzle', views.puzzle, name='puzzle'), # Пазлы
    path('/search', views.search, name='search'), # Поиск
    path('', views.feed, name='feed'), # Главное
    path('/playlists', views.playlists, name='playlists'), # Плейлисты
    path('/subscription', views.subscription, name='subscription'), # Подписка

    path('/data', views.data, name='account_data'), # Подписка
    path('/card', views.card, name='account_card'), # Подписка

]