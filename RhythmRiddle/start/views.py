
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h4>Основная страница</h4>")

def about(request):
    return HttpResponse("<h4>О нас</h4>")

def advertising(request):
    return HttpResponse("<h4>Реклама</h4>")

def rules(request):
    return HttpResponse("<h4>Пользовательское соглашение</h4>")

def subscription(request):
    return HttpResponse("<h4>Подписка</h4>")

def support(request):
    return HttpResponse("<h4>Поддержка</h4>")
