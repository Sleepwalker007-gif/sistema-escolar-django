from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("alunos/", views.lista_alunos, name="alunos"),
    path("cursos/", views.lista_cursos, name="cursos"),
]
