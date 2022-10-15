from django.contrib import admin
from .models import TipoSangue
# Register your models here.


class TipoSangueAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo')
    search_fields = ('tipo',)


admin.site.register(TipoSangue, TipoSangueAdmin)

