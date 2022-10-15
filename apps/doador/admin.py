from django.contrib import admin
from .models import Doador


class DoadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'data_nascimento', 'tipo_sangue', 'email',
                    'telefone', 'provincia', 'hospital', 'ultimo_log')
    search_fields = ('nome', 'sobrenome')
    list_filter = ('nome', 'sobrenome')
    autocomplete_fields = ('hospital', 'provincia', 'tipo_sangue', 'user')


admin.site.register(Doador, DoadorAdmin)
