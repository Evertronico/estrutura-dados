def inserir_ordenado(lista, valor):

    #encontra a posição correta
    pos = 0
    while pos < len(lista) and lista[pos] < valor:
        pos += 1

    # aumenta o tamanho da lista
    lista.append(0)

    #deslocar elementos para direita
    for i in range(len(lista)-1, pos, -1):
        lista[i] = lista[i-1]

    #insere o valor
    lista[pos] = valor

    return lista


numeros = [10, 20, 40, 50]

numeros = inserir_ordenado(numeros, 30)

print(numeros)