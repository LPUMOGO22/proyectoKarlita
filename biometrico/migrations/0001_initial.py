# Generated by Django 5.0.6 on 2024-06-19 12:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Empleado",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("apellido", models.CharField(max_length=100)),
                ("fecha_nacimiento", models.DateField()),
                ("direccion", models.CharField(max_length=100)),
                ("telefono", models.CharField(max_length=100)),
                ("correo", models.CharField(max_length=100)),
                ("puesto", models.CharField(max_length=100)),
                ("usuario", models.CharField(max_length=100)),
                ("contrasena", models.CharField(max_length=100)),
                ("fecha_creacion", models.DateTimeField(auto_now_add=True)),
                ("fecha_actualizacion", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Membresia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("precio", models.DecimalField(decimal_places=2, max_digits=10)),
                ("descripcion", models.TextField()),
                ("fecha_creacion", models.DateTimeField(auto_now_add=True)),
                ("fecha_actualizacion", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Usuario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("apellido", models.CharField(max_length=100)),
                ("fecha_nacimiento", models.DateField()),
                ("direccion", models.CharField(max_length=100)),
                ("telefono", models.CharField(max_length=100)),
                ("correo", models.CharField(max_length=100)),
                ("membresia", models.CharField(max_length=100)),
                ("fecha_creacion", models.DateTimeField(auto_now_add=True)),
                ("fecha_actualizacion", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="RegistroBiometrico",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha", models.DateField()),
                (
                    "foto",
                    models.ImageField(blank=True, null=True, upload_to="usuarios"),
                ),
                ("fecha_creacion", models.DateTimeField(auto_now_add=True)),
                ("fecha_actualizacion", models.DateTimeField(auto_now=True)),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="biometrico.usuario",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Acceso",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha", models.DateField()),
                ("hora", models.TimeField()),
                ("tipo", models.CharField(max_length=100)),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="biometrico.usuario",
                    ),
                ),
            ],
        ),
    ]
