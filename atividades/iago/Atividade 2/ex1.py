# Atividade 2 - Ex 1: Cadastro e Busca
alunos = ["Iago", "Daniel", "Fellipe", "Mateus"]

def buscar_aluno(lista, nome):
    for i in range(len(lista)):
        if lista[i] == nome:
            return i
    return -1

def adicionar_aluno(lista, nome):
    lista[:] = lista + [nome]
    print(f"Aluno {nome} registado!")

# Teste
nome_busca = "Iago"
pos = buscar_aluno(alunos, nome_busca)
print(f"Resultado da busca por {nome_busca}: Posição {pos}")