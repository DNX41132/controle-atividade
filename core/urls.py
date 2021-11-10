from django.urls import path

from .views import index, aluno, disciplinas

urlpatterns = [
    path('', index, name='index'),
    path('aluno/', disciplinas, name='aluno'),
    path('disciplinas/', aluno, name='disciplinas'),
    ]