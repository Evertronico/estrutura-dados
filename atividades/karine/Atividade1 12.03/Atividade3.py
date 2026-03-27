def remover(lista, valor):

    indice_encontrado = -1 
    for i in range(len(lista)):
        if lista[i] == valor:
            indice_encontrado = i
            break
    
    if indice_encontrado == -1:
        print("Valor não encontrado na lista.")
        return lista

    for i in range(indice_encontrado, len(lista) - 1):
        lista[i] = lista[i + 1]

    resultado = lista[:-1]
    
    return resultado

lista = [1, 15, 267, 80, 7, 21, 20, 33, 91, 180]
remocao = 267

nova_lista = remover(lista, remocao)
print(f"Lista atualizada: {nova_lista}")