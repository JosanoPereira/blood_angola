# Generated by Django 4.1.2 on 2022-10-18 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("familiar", "0005_alter_familiar_nome_alter_familiar_tipo_sangue_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="familiar",
            name="data_nascimento",
            field=models.DateField(verbose_name="Data de Nascimento"),
        ),
    ]
