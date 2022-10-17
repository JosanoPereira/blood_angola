from django.contrib.auth.models import User
from django.db import models
from apps.tipo_sangue.models import TipoSangue
from apps.provincias.models import Provincia
from apps.hospital.models import Hospital


class Doador(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Primeiro nome')
    sobrenome = models.CharField(max_length=150, verbose_name='Sobrenome')
    data_nascimento = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='Data de Nascimento')
    tipo_sangue = models.ForeignKey(TipoSangue, on_delete=models.DO_NOTHING)
    email = models.EmailField(max_length=150, verbose_name='E-mail')
    telefone = models.CharField(max_length=25, verbose_name='Número de Telefone')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    provincia = models.ForeignKey(Provincia, on_delete=models.DO_NOTHING, verbose_name='Província')
    hospital = models.ForeignKey(Hospital, on_delete=models.DO_NOTHING, verbose_name='Hospital')
    ultimo_log = models.DateTimeField(auto_now=True, verbose_name='Último Login')

    def __str__(self):
        return self.nome + ' ' + self.sobrenome


class HospitalDoador(models.Model):
    doador = models.ForeignKey(Doador, on_delete=models.PROTECT)
    hospital = models.ForeignKey(Hospital, on_delete=models.PROTECT)
    tipo_sangue = models.ForeignKey(TipoSangue, on_delete=models.PROTECT)
    ultima_doacao = models.DateField(auto_created=True, auto_now=True)

    def __str__(self):
        return f'{self.doador} ({self.hospital})'