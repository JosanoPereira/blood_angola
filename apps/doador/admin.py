from django.contrib import admin
from .models import Doador, HospitalDoador


class DoadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'data_nascimento', 'tipo_sangue', 'email',
                    'telefone', 'provincia', 'hospital', 'ultimo_log', 'id')
    search_fields = ('nome', 'sobrenome')
    list_filter = ('nome', 'sobrenome')
    autocomplete_fields = ('hospital', 'provincia', 'tipo_sangue', 'user')


class HospitalDoadorAdmin(admin.ModelAdmin):
    list_display = ('doador', 'hospital', 'tipo_sangue', 'ultima_doacao')
    search_fields = ('doador', 'hospital')
    autocomplete_fields = ('hospital', 'tipo_sangue', 'doador')


admin.site.register(Doador, DoadorAdmin)
admin.site.register(HospitalDoador, HospitalDoadorAdmin)
