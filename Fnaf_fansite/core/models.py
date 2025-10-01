from django.db import models


class Personaje(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    nivel_miedo = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(upload_to="personajes/")

    def __str__(self):
        return self.nombre

