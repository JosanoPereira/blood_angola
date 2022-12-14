from django.db import models
from apps.provincias.models import Provincia
# from apps.doador.models import Doador
# from apps.tipo_sangue.models import TipoSangue


class Hospital(models.Model):
    nome = models.CharField(max_length=200, verbose_name='Nome do Hospital')
    provincia = models.ForeignKey(Provincia, on_delete=models.DO_NOTHING, verbose_name='Província')

    def __str__(self):
        return f'{self.nome} ({self.provincia})'


