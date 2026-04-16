TAMANHO_MAX = 10

def criar_lista():
    return [None] * TAMANHO_MAX

def inserir(lista, qtd, valor, pos):
    if qtd >= TAMANHO_MAX:
        print("Lista cheia!")
        return qtd

    if pos < 0 or pos > qtd:
        print("Posição inválida!")
        return qtd

    for i in range(qtd, pos, -1):
        lista[i] = lista[i - 1]

    lista[pos] = valor
    return qtd + 1

def remover(lista, qtd, pos):
    if qtd == 0:
        print("Lista vazia!")
        return qtd

    if pos < 0 or pos >= qtd:
        print("Posição inválida!")
        return qtd

    for i in range(pos, qtd - 1):
        lista[i] = lista[i + 1]

    lista[qtd - 1] = None
    return qtd - 1

def buscar(lista, qtd, valor):
    for i in range(qtd):
        if lista[i] == valor:
            return i
    return -1

def exibir(lista, qtd):
    for i in range(qtd):
        print(lista[i])

lista = criar_lista()
qtd = 0