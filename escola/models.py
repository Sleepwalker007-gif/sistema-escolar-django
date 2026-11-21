from django.db import models

class Curso(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)

    class Meta:
        ordering = ["titulo"]
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.titulo


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    cursos = models.ManyToManyField(Curso, related_name="alunos", blank=True)

    class Meta:
        ordering = ["nome", "sobrenome"]
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
