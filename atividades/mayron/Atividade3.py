dados = [10, 20, 30, 40, 50]

def remover(lista, valor):
    indice = -1

    for i in range(len(lista)):
        if lista[i] == valor:
            indice = i
            break

    if indice != -1:
        
        for i in range(indice, len(lista) - 1):
            lista[i] = lista[i + 1]

        del lista[-1]

remover(dados, 30)
print(dados)
