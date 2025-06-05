from django.shortcuts import render, redirect, reverse
from django import http
from authorization import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


def login_user(request: http.HttpRequest) -> http.HttpResponse:
    if request.user.is_authenticated:
        return redirect(reverse('home_page'))

    if request.method == 'GET':
        form = forms.LoginForm()
        return render(
            request,
            'pages/form.html',
            {
                'form': form,
                'button_text': 'Войти'
            }
        )

    form = forms.LoginForm(request.POST)
    if not form.is_valid():
        return render(
            request,
            'pages/form.html',
            {
                'form': form,
                'button_text': 'Войти'
            }
        )

    user: User = authenticate(request, form.username, form.password)
    if not user:
        messages.error(
            request,
            'Пароль неправильный'
            if User.objects.filter(username=form.username).count()
            else "Неправильное имя пользователя"
        )
        return render(
            request,
            'pages/form.html',
            {
                'form': form,
                'button_text': 'Войти'
            }
        )
    messages.success(request, f'Добро пожаловать, {user.first_name}')
    login(request, user)

    return redirect(reverse('home_page'))


def register_user(request: http.HttpRequest) -> http.HttpResponse:
    if request.method == 'GET':
        form = forms.RegisterForm()
        return render(
            request,
            'pages/form.html',
            {
                'form': form,
                'button_text': 'Зарегистрироваться'
            }
        )

    form = forms.RegisterForm(request.POST)
    if not form.is_valid():
        return render(
            request,
            'pages/form.html',
            {
                'form': form,
                'button_text': 'Зарегистрироваться'
            }
        )

    user: User = form.save(commit=False)
    user.username = user.username.lower()
    user.save()

    login(request, user)

    return redirect(reverse('home_page'))


def logout_user(request: http.HttpRequest) -> http.HttpResponse:
    if request.user.is_authenticated:
        logout(request)

    return redirect(reverse('home_page'))
