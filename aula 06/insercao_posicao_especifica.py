def inserir_posicao(lista, valor, posicao):
    if posicao < 0 or posicao > len(lista):
        raise IndexError("Posição inválida")

    # Adiciona elemento fictício ao final para expandir lista
    lista.append(None)

    # Desloca elementos da direita para esquerda
    for i in range(len(lista) - 1, posicao, -1):
        lista[i] = lista[i - 1]

    lista[posicao] = valor

dados = [10, 20, 30, 40]
inserir_posicao(dados, 25, 2)
print(dados)