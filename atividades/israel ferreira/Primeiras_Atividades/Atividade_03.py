'''
    Atividade 3 — Remoção Manual de Elemento
    Implemente uma função que remova um elemento de uma lista sem utilizar métodos prontos.
    Função esperada:
    remover(lista, valor)
    O algoritmo deve:
    localizar o elemento
    deslocar os elementos à direita
    atualizar a lista resultante
    Não utilizar:
    remove()
    pop()
'''
def remover(lista, elemento):
    if elemento < 0 or elemento >= len(lista):
        raise IndexError("Posição inválida")

    for i in range(elemento, len(lista) - 1):
        lista[i] = lista[i + 1]

    nova = [lista[i] for i in range(len(lista) - 1)]

    lista[:] = nova


dados = [1, 11, 22, 33, 44, 55, 66]
remover(dados, 2)
print(dados)  