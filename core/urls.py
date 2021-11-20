from django.urls import path

from .views import index, aluno, disciplinas

urlpatterns = [
    path('', index, name='index'),
    path('aluno/', aluno, name='aluno'),
    path('disciplinas/', disciplinas, name='disciplinas'),
    ]