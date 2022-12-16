from django.shortcuts import render
from .models import BlogPost


def index(request):
    return render(request, 'index.html', {})


def games(request):
    context = {
        'posts': BlogPost.objects.all()
    }
    return render(request, 'games.html', context)


def channels(request):
    return render(request, 'channels.html', {})

# Create your views here.
