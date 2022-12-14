# Generated by Django 4.1.2 on 2022-10-17 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("doador", "0008_rename_tipe_sangue_hospitaldoador_tipo_sangue"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doador",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Usuário",
            ),
        ),
    ]
