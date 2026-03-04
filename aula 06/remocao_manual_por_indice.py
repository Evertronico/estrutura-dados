def remover_posicao(lista, posicao):
    if posicao < 0 or posicao >= len(lista):
        raise IndexError("Posição inválida")

    # Desloca elementos à esquerda
    for i in range(posicao, len(lista) - 1):
        lista[i] = lista[i + 1]

    # Remove último elemento duplicado
    lista.pop()

dados = [5, 15, 25, 35, 45]
remover_posicao(dados, 2)
print(dados)