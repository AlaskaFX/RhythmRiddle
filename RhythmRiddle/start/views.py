
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse # удалить когда допилю страницы
from .forms import RegistrationForm

def index(request):
    return render(request, 'start/index.html')

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

###

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/main')
    else:
        form = RegistrationForm()
    return render(request, 'start/register.html', {'form': form})

