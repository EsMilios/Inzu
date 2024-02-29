from django.db import models

class usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nombreUsuario = models.CharField(max_length=50)
    telefonoUsuario = models.CharField(max_length=10)
    emailUsuario = models .EmailField(unique=True)
    direccionUsuario = models.CharField(max_length=15)


