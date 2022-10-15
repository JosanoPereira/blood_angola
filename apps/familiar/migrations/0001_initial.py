# Generated by Django 4.1.2 on 2022-10-09 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("hospital", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tipo_sangue", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Familiar",
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
                (
                    "nome",
                    models.CharField(max_length=150, verbose_name="Nome do Doador:"),
                ),
                (
                    "data_nascimento",
                    models.DateTimeField(verbose_name="Data de Nascimento:"),
                ),
                ("email", models.EmailField(max_length=150, verbose_name="E-mail:")),
                (
                    "telefone",
                    models.CharField(max_length=25, verbose_name="Número de Telefone:"),
                ),
                (
                    "hospital",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hospital.hospital",
                    ),
                ),
                (
                    "tipo_sangue",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="tipo_sangue.tiposangue",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
