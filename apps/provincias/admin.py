from django.contrib import admin
from .models import Provincia
# Register your models here.


class ProvinciasAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)


admin.site.register(Provincia, ProvinciasAdmin)
