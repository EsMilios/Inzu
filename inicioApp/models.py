from django.db import models
from PerfilApp.models import usuario

class categoriaIngreso(models.Model):
    nombreCategoriaIngreso = models.CharField(max_length=50)

class categoriaEgreso(models.Model):
    nombreCategoriaEgreso = models.CharField(max_length=50)

class egresos(models.Model):
    idEgreso = models.AutoField(primary_key=True)
    montoEgreso = models.IntegerField()
    fechaEgreso = models.DateField()
    descripcionEgreso = models.TextField()

    idUsuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    nombreCategoriaEgreso = models.ForeignKey(categoriaEgreso, on_delete=models.CASCADE)


class ingreso(models.Model):
    idIngreso = models.AutoField(primary_key=True)
    nombreIngreso = models.CharField(max_length=50)
    montoIngreso = models.IntegerField()
    fechaIngreso = models.DateField()
    descripcionIngreso = models.TextField()

    idUsuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    nombreCategoriaIngreso = models.ForeignKey(categoriaIngreso, on_delete=models.CASCADE)
