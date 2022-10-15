from django.db import models
from apps.doador.models import Doador


# Create your models here.

class Documento(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nº documentos:', unique=True)
    dono = models.ForeignKey(Doador, on_delete=models.PROTECT, verbose_name='Proprietário')
    file = models.FileField(upload_to='documentos', verbose_name='Ficheiro')

    def __str__(self):
        return f'{self.nome} ({self.dono})'
