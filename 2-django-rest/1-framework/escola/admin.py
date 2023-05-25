from django.contrib import admin
from escola.models import Aluno, Curso


# As configurações nessa classe só valem para o Django Admin -> interface de administração imbutida no django e é
# gerada de forma automática. As informações aqui não estão no formato Json, para isso é preciso fazer uma ponte
# utilizando um serializer. Ele transforma informações que o django entende para o json e vice-versa

class Alunos(admin.ModelAdmin):
    list_display: tuple[str, str, str, str, str] = ('id', 'nome', 'rg', 'cpf', 'data_nascimento') # Retorno para admin -> se "assemelha" a um DTO em java
    list_display_links: tuple[str, str] = ('id', 'nome') # Abre a possibilidade de alterar ou editar um aluno clicando em -> id, nome
    search_fields = ('nome', )   # configura a possibílidade de buscar um aluno por nome -> Se assemelha a uma @Query() personalizada
    list_per_page = 20 # Paginação -> semelhante ao Page em java


admin.site.register(Aluno, Alunos) # Registra a configuração no admin


class Cursos(admin.ModelAdmin):
    list_display: tuple[str, str, str] = ('id', 'codigo_curso', 'descricao')
    list_display_links: tuple[str, str] = ('id', 'codigo_curso')
    search_fields = ('codigo_curso',)
    list_per_page = 10


admin.site.register(Curso, Cursos)
