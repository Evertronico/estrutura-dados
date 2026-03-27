def inserir_ordenado(lista, valor):
    posicao = 0
    
    while posicao < len(lista) and lista[posicao] < valor:
        posicao += 1

    lista.append(None)

    for i in range(len(lista) - 1, posicao, -1):
        lista[i] = lista[i - 1]

    lista[posicao] = valor

numeros = [2032, 5659, 1396, 3265]
print("Antes:", numeros)
inserir_ordenado(numeros, 2589)
inserir_ordenado(numeros, 3265)
print("Depois:", numeros)