from django.contrib import admin
from .models import Hospital
# Register your models here.


class HospitalAdmin(admin.ModelAdmin):
    search_fields = ('nome',)
    list_display = ('nome', 'provincia')
    autocomplete_fields = ('provincia',)


admin.site.register(Hospital, HospitalAdmin)
