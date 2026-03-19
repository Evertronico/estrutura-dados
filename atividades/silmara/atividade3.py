# Atividade 3 — Remoção Manual de Elemento
# Implemente uma função que remova um elemento de uma lista sem utilizar métodos prontos.
# Função esperada:
# remover(lista, valor)
# O algoritmo deve:
# localizar o elemento
# deslocar os elementos à direita
# atualizar a lista resultante
# Não utilizar:
# remove()
# pop()

lista = [20, 45, 88, 751, 0.0, 0.1]
qtde_lista = len(lista)

def remover(lista, valor):
    for i in range(qtde_lista):
        if lista[i] == valor:
            for j in range(i, qtde_lista - 1):
                lista[j] = lista[j + 1]
            del lista[-1]
            return lista
    return lista

print(remover(lista, 45))
