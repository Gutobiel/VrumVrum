from django.db import models

class Semaforo(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    endereco = models.CharField(max_length=255)
    tipo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)

    def __str__(self):
        return self.codigo