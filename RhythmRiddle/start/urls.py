
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), # Начальная страница
    path('about', views.about), # О нас
    path('advertising', views.advertising), # Реклама
    path('rules', views.rules), # Правила
    path('subscription', views.subscription), # Правила
    path('support', views.support), # Правила
]
