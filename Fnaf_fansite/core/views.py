from django.shortcuts import render
from .models import Personaje

def home(request):
    return render(request, "core/home.html")

def foro(request):
    return render(request, "core/foro.html")

def quest(request):
    return render(request, "core/quest.html")

def gallery(request):
    return render(request, "core/gallery.html")

def personajes(request):
    personajes = Personaje.objects.all()
    return render(request, "core/personajes.html", {"personajes": personajes})
