from datetime import datetime
from django.db import models


class Aluno(models.Model):
    nome: str = models.CharField(max_length=30)
    rg: str = models.CharField(max_length=9)
    cpf: str = models.CharField(max_length=11)
    data_nascimento: datetime = models.DateField()

    def __str__(self):
        return self.nome


class Curso(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado')
    )
    codigo_curso: str = models.CharField(max_length=10)
    descricao: str = models.CharField(max_length=100)
    nivel: NIVEL = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B')

    def __str__(self):
        return self.descricao
