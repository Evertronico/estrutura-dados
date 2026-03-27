def remover(lista, valor):
    indice = -1
    for i in range(len(lista)):
        if lista[i] == valor:
            indice = i
            break

    if indice == -1:
        return lista

    for i in range(indice, len(lista) - 1):
        lista[i] = lista[i + 1]

    nova_lista = []
    for i in range(len(lista) - 1):
        nova_lista.append(lista[i])

    return nova_lista


numeros = [10, 20, 30, 40, 50]
resultado = remover(numeros, 30)

print("Lista original:", numeros)
print("Lista após remoção:", resultado)