# Exercício 1 – Cadastro de Alunos com Operações Básicas
# Implemente um sistema para gerenciamento de alunos de uma turma utilizando listas em Python. O sistema deve permitir o controle completo dos alunos cadastrados.
# Requisitos:
#  * Armazenar os alunos em uma lista
#  * Implementar função para adicionar aluno
#  * Implementar função para buscar aluno pelo nome (sem usar in ou index)
#  * Implementar função para remover aluno manualmente (sem remove)
#  * Exibir todos os alunos cadastrados

alunos = []

def adicionar_aluno(nome):
    alunos.append(nome)

def buscar_aluno(nome):
    for i in range(len(alunos)):
        if alunos[i] == nome:
            return i
        
def remover_aluno(nome):
    posicao = buscar_aluno(nome)
    if posicao != -1:
        for i in range(posicao, len(alunos) - 1):
            alunos[i] = alunos[i + 1]
        alunos.pop()
        print(f"Aluno {nome} removido")
    else:
        print("Aluno não encontrado")
    
def exibir_alunos():
    print(f"Lista de Alunos: {alunos}")

adicionar_aluno('Silmara')
adicionar_aluno('Lucky')
adicionar_aluno('Felps')
adicionar_aluno('Pompom')
exibir_alunos()

posicao = buscar_aluno('Felps')
print(f'Aluno encontrado na posição {posicao}')

remover_aluno('Lucky')
exibir_alunos()
