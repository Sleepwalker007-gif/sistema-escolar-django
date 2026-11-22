from django.contrib import admin
from .models import Aluno, Curso


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("titulo",)
    search_fields = ("titulo", "descricao")


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ("nome", "sobrenome", "email")
    search_fields = ("nome", "sobrenome", "email")
    list_filter = ("cursos",)
    filter_horizontal = ("cursos",)
