
from django.contrib import admin
from .models import Personaje

@admin.register(Personaje)
class PersonajeAdmin(admin.ModelAdmin):
    list_display = ("nombre", "nivel_miedo", "fecha_creacion", "fecha_actualizacion")
    search_fields = ("nombre",)
    list_filter = ("nivel_miedo", "fecha_creacion")
