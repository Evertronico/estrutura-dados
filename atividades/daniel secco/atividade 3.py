def remover(lista, valor):

    indice = -1
# vê se o valor existe na lista e onde
    for i in range(len(lista)):
        if lista[i] == valor:
            indice = i
            break
    if indice == -1:
        return lista
    
    # remove o valor da litsa
    for i in range(indice, len(lista) - 1):
        lista[i] = lista[i +1]
        
    del lista[len(lista) - 1]
    
    return lista



lista = [10009, 2836, 92, 8, 2183736, 28, 10]
remover(lista, 10009)
print(lista)
        
