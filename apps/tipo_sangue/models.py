from django.db import models

class TipoSangue(models.Model):
    tipo = models.CharField(max_length=50,
                            null=False,
                            blank=False,
                            verbose_name='Tipo Sanguineo')

    def __str__(self):
        return self.tipo