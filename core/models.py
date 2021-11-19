from django.db import models



class Aluno(models.Model):
    nome = models.CharField('Nome', max_length=100)
    atividades = models.IntegerField('Numero de Atividades dadas')
    n_entregues = models.IntegerField('Numero de Atividades não entregues')
    faltas = models.IntegerField('Faltas')
    descricao_atv = models.TextField('Descrição das atividades', max_length=5000)
    evol_aluno = models.TextField('Evolução do aluno', max_length=200)
    atv_pendente = models.TextField('Atividades pendentes', max_length=200)

    def __str__(self):
        return self.nome