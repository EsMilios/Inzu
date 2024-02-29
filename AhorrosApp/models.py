from django.db import models
from inicioApp.models import ingreso

class categoriaAhorro(models.Model):
    nombreCategoriaAhorro = models.CharField(max_length=50)

class ahorro(models.Model):
    idAhorro = models.AutoField(primary_key=True)
    nombreAhorro = models.CharField(max_length=50)
    fechaAhorro = models.DateField()

    nombreCategoriaAhorro = models.ForeignKey(categoriaAhorro, on_delete=models.CASCADE)

class tieneIngresoAhorro(models.Model):
    idTieneIngresoAhorro = models.AutoField(primary_key=True)
    ahorro = models.ForeignKey(ahorro, on_delete=models.CASCADE)
    ingreso = models.ForeignKey(ingreso, on_delete=models.CASCADE)
