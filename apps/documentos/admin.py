from django.contrib import admin
from .models import Documento

# Register your models here.


class DocumentosAdmmin(admin.ModelAdmin):
    list_display = ('nome', 'dono', 'file')
    autocomplete_fields = ('dono',)


admin.site.register(Documento,DocumentosAdmmin)
