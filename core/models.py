from django.db import models



class Aluno(models.Model):
    nome = models.CharField('Nome', max_length=100)
    atividades = models.IntegerField('Atividades', max_length=500)
    n_entregues = models.IntegerField('Atividades não entregues', max_length=500)
    faltas = models.IntegerField('Faltas', max_length=100)
    descricao_atv = models.TextField('Descrição das atividades', max_length=5000)
    evol_aluno = models.TextField('Evolução do aluno', max_length=5000)