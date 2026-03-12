#remocao manual de um item pelo indice
def remover_posicao(lista, posicao):
    #verifica se a posição informada é válida
    if posicao < 0 or posicao >= len(lista):
        raise IndexError("Posição Informada para remoção é inválida")
    
    #desloca elementos à esquerda
    for i in range(posicao, len(lista) -1):
        lista[i] = lista[i + 1]

    #remove o último elemento duplicado
    lista.pop()

dados = [5, 15, 25, 35, 45]
remover_posicao(dados, 2) 
print(dados)