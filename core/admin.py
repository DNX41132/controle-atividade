from django.contrib import admin

from .models import Aluno

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'atividades', 'n_entregues', 'faltas', 'atv_pendente', 'evol_aluno')

admin.site.register(Aluno, AlunoAdmin)
admin.site.site_header = 'Controle de Atividade'

