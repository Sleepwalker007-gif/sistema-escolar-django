from django.shortcuts import render
from .models import Aluno, Curso


def inicio(request):
    contexto = {
        "total_alunos": Aluno.objects.count(),
        "total_cursos": Curso.objects.count(),
    }
    return render(request, "escola/inicio.html", contexto)


def lista_alunos(request):
    alunos = Aluno.objects.prefetch_related("cursos").all()
    return render(request, "escola/alunos.html", {"alunos": alunos})


def lista_cursos(request):
    cursos = Curso.objects.prefetch_related("alunos").all()
    return render(request, "escola/cursos.html", {"cursos": cursos})
