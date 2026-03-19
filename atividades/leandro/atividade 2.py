def buscaSequencial(lista,valor):
    achou = False
    for x in range(len(lista)):
        if lista[x] == valor:
            achou = True
            return print(f" O elemento {valor} foi encontrado no indice {x}")
    if not achou:
        return print("-1")
    
lista = [10, 5, 6, 8, 9, 1, 7]

buscaSequencial(lista,10)