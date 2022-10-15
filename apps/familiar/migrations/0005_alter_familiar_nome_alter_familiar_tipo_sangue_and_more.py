# Generated by Django 4.1.2 on 2022-10-09 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tipo_sangue", "0001_initial"),
        ("familiar", "0004_familiar_ultimo_log"),
    ]

    operations = [
        migrations.AlterField(
            model_name="familiar",
            name="nome",
            field=models.CharField(max_length=150, verbose_name="Nome"),
        ),
        migrations.AlterField(
            model_name="familiar",
            name="tipo_sangue",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="tipo_sangue.tiposangue",
                verbose_name="Tipo Sanguíneo",
            ),
        ),
        migrations.AlterField(
            model_name="familiar",
            name="ultimo_log",
            field=models.DateTimeField(auto_now=True, verbose_name="Último Login"),
        ),
    ]