from rest_framework import serializers
from escola.models import Aluno, Curso


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model: Aluno = Aluno
        fields: tuple[str, str, str, str, str] = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model: Curso = Curso
        fields: str = '__all__'  # retorna todas as informações de um curso