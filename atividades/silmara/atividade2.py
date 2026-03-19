# Atividade 2 — Busca Sequencial
# Implemente uma função chamada:
# busca_sequencial(lista, valor)
# A função deve percorrer a lista e retornar:
# o índice do elemento encontrado
# -1 caso o valor não esteja presente.
# Não utilize:
# index()
# in

lista = [13, 67, 973, 0.5, 20, 70, 99]
qtde_lista = len(lista)

def busca_sequencial(lista, valor):
    for i in range(qtde_lista):
        if lista[i] == valor:
            return i
    return -1

print(busca_sequencial(lista, 973))
