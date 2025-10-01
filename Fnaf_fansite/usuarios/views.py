from django.shortcuts import render
from .models import PerfilUsuario

def lista_usuarios(request):
    usuarios = PerfilUsuario.objects.all()
    return render(request, "usuarios/lista.html", {"usuarios": usuarios})
