from django.contrib import admin
from .models import Familiar
# Register your models here.


class FamiliarAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_nascimento', 'tipo_sangue', 'email',
                    'telefone', 'ultimo_log')
    search_fields = ('nome',)
    list_filter = ('nome',)
    autocomplete_fields = ('hospital', 'tipo_sangue', 'user')


admin.site.register(Familiar, FamiliarAdmin)
