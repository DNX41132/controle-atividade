from django.urls import path

from .views import index, aluno, disciplinas

urlpatterns = [
    path('', index, name='index'),
    path('contato/', disciplinas, name='contato'),
    path('produto/', aluno, name='produto'),
    ]