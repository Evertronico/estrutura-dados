from random import randint

def inserir_ordenado(lista, valor):
    posicao = len(lista)

    for x in range(len(lista)):
        if lista[x] > valor:
            posicao = x
            break

    lista.append(None)
    
    for y in range(len(lista) - 1, posicao, -1):
        lista[y] = lista[y -1]

    lista[posicao] = valor

lista = list()

for i in range(10):
    inserir_ordenado(lista, randint(0, 10))

print(lista)