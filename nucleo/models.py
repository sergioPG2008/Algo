from django.db import models

class Client(models.Model):

    nombre = models.CharField(max_length=100)

    apellidos = models.CharField(max_length=100)

    telefono = models.CharField(max_length=100)

    gmail = models.EmailField(max_length=100)

    direccion = models.CharField(max_length=100)

    plantaFav = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellidos} y te gustan {self.plantaFav}"
