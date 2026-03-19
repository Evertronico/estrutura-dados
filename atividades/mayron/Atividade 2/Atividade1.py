alunos = []

def adicionar_aluno(nome):
    alunos.append(nome)
    print("Aluno", nome, "cadastrado com sucesso.")

def buscar_aluno(nome):
    for i in range(len(alunos)):
        if alunos[i] == nome:
            return i
    return -1

def remover_aluno(nome):
    indice = buscar_aluno(nome)
    if indice != -1:
        for i in range(indice, len(alunos) - 1):
            alunos[i] = alunos[i + 1]
        
        alunos.pop()
        print("Aluno", nome, "removido.")
    else:
        print("Aluno não encontrado.")

def exibir_alunos():
    for i in range(len(alunos)):
        print(f"Posição {i}: {alunos[i]}")

# Testando
adicionar_aluno("João")
adicionar_aluno("Maria")
exibir_alunos()
remover_aluno("João")
exibir_alunos()