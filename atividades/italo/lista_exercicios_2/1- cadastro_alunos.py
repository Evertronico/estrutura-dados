alunos = []

def adicionar_aluno(lista, nome):
    lista.append(nome)

def buscar_aluno(lista, nome):
    for i in range(len(lista)):
        if lista[i] == nome:
            return i
    return -1

def remover_aluno(lista, nome):
    indice = buscar_aluno(lista, nome)

    if indice == -1:
        return lista

    for i in range(indice, len(lista) - 1):
        lista[i] = lista[i + 1]

    nova_lista = []
    for i in range(len(lista) - 1):
        nova_lista.append(lista[i])

    return nova_lista

def exibir_alunos(lista):
    if len(lista) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        print("Lista de alunos:")
        for aluno in lista:
            print("-", aluno)


adicionar_aluno(alunos, "Ana")
adicionar_aluno(alunos, "Carlos")
adicionar_aluno(alunos, "Beatriz")

exibir_alunos(alunos)

print("\nBuscando 'Carlos'")
pos = buscar_aluno(alunos, "Carlos")
print("Encontrado no índice:", pos)

print("\nRemovendo 'Carlos'...")
alunos = remover_aluno(alunos, "Carlos")

exibir_alunos(alunos)