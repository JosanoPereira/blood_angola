from django.contrib.auth.models import User
from django.db import models
from apps.hospital.models import Hospital
from apps.tipo_sangue.models import TipoSangue


class Familiar(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome')
    data_nascimento = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Data de Nascimento')
    tipo_sangue = models.ForeignKey(TipoSangue, on_delete=models.DO_NOTHING, verbose_name='Tipo Sanguíneo')
    email = models.EmailField(max_length=150, verbose_name='E-mail')
    telefone = models.CharField(max_length=25, verbose_name='Número de Telefone')
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, verbose_name='Hospital')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    ultimo_log = models.DateTimeField(auto_now=True, verbose_name='Último Login')
