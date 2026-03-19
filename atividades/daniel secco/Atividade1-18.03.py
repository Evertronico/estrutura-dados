alunos = []


def adiciona(nome):
    alunos.append(nome)

def buscar(nome):
    for aluno in alunos:
        if aluno == nome:
            return True
        return False
    
def remover(nome):
    novalista = []
    for aluno in alunos:
        if aluno != nome:
            novalista.append(aluno)
        return novalista
    
def listar():
    for aluno in alunos:
        print(aluno)
    