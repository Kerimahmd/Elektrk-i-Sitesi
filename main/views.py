from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'title': 'ALYANS ELEKTRİK',
        'content': 'ALYANS ELEKTRİK',
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Hakkımızda',
    }
    return render(request, 'main/about.html', context)


def projects(request):
    context = {
        "title": "Projeler",
    }
    return render(request, 'main/projects.html', context)

