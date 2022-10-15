from django.db import models


class Provincia(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Província')

    def __str__(self):
        return self.nome
