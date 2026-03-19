# * Armazenar os alunos em uma lista
# * Implementar função para adicionar aluno
# * Implementar função para buscar aluno pelo nome (sem usar in ou index)
# * Implementar função para remover aluno manualmente (sem remove)
# * Exibir todos os alunos cadastrados

listaAlunos = ["Juca", "Daniel", "Jeff"]

def addAluno(aluno):
    if(aluno == ''):
        print("O valor do aluno deverá ser válido")
        return 
    listaAlunos.append(aluno)

def buscarAluno(aluno):
    i = 0
    while (listaAlunos.length - 1 > i):
        if(listaAlunos[i] == aluno):
            print(aluno)
        else:
            i = i + 1


def removerAluno(nomeAluno):
    global listaAlunos
    listaSemAluno = []
    for aluno in listaAlunos:
        if(aluno == nomeAluno):
            continue
        else:
            listaSemAluno.append(aluno)
    
    listaAlunos = listaSemAluno


def exibirAlunosCadastrados():
    print("Lista de alunos" + "\n")
    for aluno in listaAlunos:
        print("Nome do aluno: " + aluno + "\n")

print("Lista Inicial")
print(listaAlunos)
addAluno("Pirado")
print("Lista com mais 1")
print(listaAlunos)
removerAluno("Pirado")
print("Lista com pirado removido")
print(listaAlunos)
exibirAlunosCadastrados()