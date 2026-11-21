from django.contrib import admin
from .models import Aluno, Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "descricao")
    search_fields = ("titulo",)

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ("nome", "sobrenome", "email")
    search_fields = ("nome", "sobrenome", "email")
    filter_horizontal = ("cursos",)
