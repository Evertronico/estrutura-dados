def inserir_ordenado(lista, valor):
    posicao = 0
    
    while posicao < len(lista) and lista[posicao] < valor:
        posicao += 1

    lista.append(None)

    for i in range(len(lista) - 1, posicao, -1):
        lista[i] = lista[i - 1]

    lista[posicao] = valor

numeros = [10, 20, 40, 50]
print("Antes:", numeros)
inserir_ordenado(numeros, 30)
inserir_ordenado(numeros, 5)
print("Depois:", numeros)