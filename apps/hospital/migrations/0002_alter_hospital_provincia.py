# Generated by Django 4.1.2 on 2022-10-09 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("provincias", "0002_alter_provincia_nome"),
        ("hospital", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hospital",
            name="provincia",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="provincias.provincia",
                verbose_name="Província",
            ),
        ),
    ]
