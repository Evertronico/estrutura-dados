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

def remover(lista, valor):
    pos = -1
    for i in range(len(lista)):
        if lista[i] == valor:
            pos = i
            break

    if pos == -1:
        return lista  
    for i in range(pos, len(lista) - 1):
        lista[i] = lista[i + 1]

    nova_lista = []
    for i in range(len(lista) - 1):
        nova_lista.append(lista[i])

    return nova_lista

numeros = [10, 20, 30, 40, 50]

valor = int(input("Digite o valor a remover: "))

numeros = remover(numeros, valor)

print("Lista atualizada:", numeros)