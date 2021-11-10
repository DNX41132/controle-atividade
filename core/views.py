from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def disciplinas(request):
    return render(request, 'disciplinas.html')

def aluno(request):
    return render(request, 'aluno.html')
