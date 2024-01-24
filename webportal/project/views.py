# webportal/views.py

from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def layout(request):
    return render(request, 'layout.html')


def contact(request):
    return render(request, 'contact.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def interactive_resume(request):
    return render(request, 'interactive_resume.html')


def snake_game(request):
    return render(request, 'snake_game.html')
