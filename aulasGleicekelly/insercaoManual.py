#inserção manual
def inserir_posicao(lista, valor, posicao):
    #validar para realizar a inserção
    if posicao < 0 or posicao > len(lista):
        raise IndexError("Posição é invalida para inserção.")
    
    #adiciona o elemento no final da lista para espandir o tamanho dela
    lista.append(None)
    #desloca elementos da direita para a esquerda
    for i in range(len(lista) -1, posicao, -1):
        lista[i] = lista[i - 1]
    #insere valor desejado na posição informada
    lista[posicao] = valor

valores = [10, 20, 30, 40]
inserir_posicao(valores, 25, 0)
print(valores)
