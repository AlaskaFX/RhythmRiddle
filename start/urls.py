
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Начальная страница
    path('about', views.about, name='about'), # О нас
    path('advertising', views.advertising, name='advertising'), # Реклама
    path('rules', views.rules, name='rules'), # Правила
    path('support', views.support, name='support'), # Поддержка

    path('register', views.register, name='register'), # Регистрация
    path('login', views.login_page, name='login'), # Авторизация
    path('logout', views.logout_user, name='logout'), # Выход
]
