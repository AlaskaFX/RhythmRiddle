
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse # удалить когда допилю страницы
from .forms import LoginUserForm, RegistrationForm


def index(request):
    if request.user.is_authenticated:
        return redirect('/main')
    return render(request, 'start/index.html')

def about(request):
    context = {}
    if request.user.is_authenticated:
        context['parent_template'] = 'main/layout.html'
    else:
        context['parent_template'] = 'start/layout.html'
    return render(request, 'start/about.html', context)

def advertising(request):
    context = {}
    if request.user.is_authenticated:
        context['parent_template'] = 'main/layout.html'
    else:
        context['parent_template'] = 'start/layout.html'
    return render(request, 'start/advertising.html', context)

def rules(request):
    context = {}
    if request.user.is_authenticated:
        context['parent_template'] = 'main/layout.html'
    else:
        context['parent_template'] = 'start/layout.html'
    return render(request, 'start/rules.html', context)

def support(request):
    context = {}
    if request.user.is_authenticated:
        context['parent_template'] = 'main/layout.html'
    else:
        context['parent_template'] = 'start/layout.html'
    return render(request, 'start/support.html', context)

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

def login_page(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return redirect('/main')
    else:
        form = LoginUserForm()
    return render(request, 'start/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('/main')