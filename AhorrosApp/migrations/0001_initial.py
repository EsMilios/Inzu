# Generated by Django 5.0.2 on 2024-02-28 17:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inicioApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='categoriaAhorro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCategoriaAhorro', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ahorro',
            fields=[
                ('idAhorro', models.AutoField(primary_key=True, serialize=False)),
                ('nombreAhorro', models.CharField(max_length=50)),
                ('fechaAhorro', models.DateField()),
                ('nombreCategoriaAhorro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AhorrosApp.categoriaahorro')),
            ],
        ),
        migrations.CreateModel(
            name='tieneIngresoAhorro',
            fields=[
                ('idTieneIngresoAhorro', models.AutoField(primary_key=True, serialize=False)),
                ('ahorro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AhorrosApp.ahorro')),
                ('ingreso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicioApp.ingreso')),
            ],
        ),
    ]
