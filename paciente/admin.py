from django.contrib import admin
from . import models


class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'telefone', 'contapoio', 'sessoes', 'estrategia', 'preferencia')
    search_fields = ('nome',)
    
admin.site.register(models.Paciente, PacienteAdmin)
