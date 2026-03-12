'''
    Atividade 4 — Inserção Ordenada em Lista
    Implemente uma função que insira um valor em uma lista mantendo a ordem crescente dos elementos.
    Função esperada:
    inserir_ordenado(lista, valor)
    A função deve:
    encontrar a posição correta do novo elemento
    deslocar os elementos necessários para a direita
    inserir o valor na posição correta
    Não utilizar:
    sort()
    insert()
'''

def inserir_ordenado(lista, valor):
    posicao = 0
    while posicao < len(lista) and lista[posicao] < valor:
        posicao += 1

    lista.append(None)

    for i in range(len(lista) - 1, posicao, -1):
        lista[i] = lista[i - 1]

    lista[posicao] = valor


dados = [11,22,33,44,55,66]
inserir_ordenado(dados, 25)
print(dados)