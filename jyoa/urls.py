from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import path


def to_index(request: HttpRequest):
    return render(request, 'index.html')


def to_login(request: HttpRequest):

    return render(request, 'login.html')


def to_regist(request: HttpRequest):
    return render(request, 'register.html')


def to_logout(req: HttpRequest):
    return redirect('/login/')


urlpatterns = [
    path('regist/', to_regist),
    path('login/', to_login),
    path('logout/', to_logout),
    path('', to_index),
]
