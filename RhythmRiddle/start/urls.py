
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Начальная страница
    path('about', views.about, name='about'), # О нас
    path('advertising', views.advertising, name='advertising'), # Реклама
    path('rules', views.rules, name='rules'), # Правила
    path('subscription', views.subscription, name='subscription'), # Правила
    path('support', views.support, name='support'), # Правила

    path('account', views.account, name='account'), # Аккаунт
]
