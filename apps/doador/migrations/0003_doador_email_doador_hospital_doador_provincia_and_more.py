# Generated by Django 4.1.2 on 2022-10-09 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("hospital", "0001_initial"),
        ("provincias", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tipo_sangue", "0001_initial"),
        ("doador", "0002_alter_doador_data_nascimento"),
    ]

    operations = [
        migrations.AddField(
            model_name="doador",
            name="email",
            field=models.EmailField(default=1, max_length=150, verbose_name="E-mail:"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="doador",
            name="hospital",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="hospital.hospital",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="doador",
            name="provincia",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="provincias.provincia",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="doador",
            name="telefone",
            field=models.CharField(
                default=1, max_length=25, verbose_name="Número de Telefone:"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="doador",
            name="tipo_sangue",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="tipo_sangue.tiposangue",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="doador",
            name="ultimo_log",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="doador",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="doador",
            name="data_nascimento",
            field=models.DateTimeField(verbose_name="Data de Nascimento:"),
        ),
    ]
