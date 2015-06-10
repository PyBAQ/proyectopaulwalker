from django.db import models

class Marca(models.Model):
    nombre = models.CharField(
        max_length=255
    )

    def __unicode__(self):
        return self.nombre

class Carro(models.Model):
    nombre = models.CharField(
        max_length=255
    )
    marca = models.ForeignKey(
        Marca
    )

    def __unicode__(self):
        return self.nombre


