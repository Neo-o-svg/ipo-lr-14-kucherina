
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Главная',
    }
    return render(request, 'storeApp/index.html', context)


def about(request):
    context = {
        'title': 'Об авторе',
    }
    return render(request, 'storeApp/about.html', context)


def store(request):
    context = {
        'title': 'Магазин',
    }
    return render(request, 'storeApp/store.html', context)
