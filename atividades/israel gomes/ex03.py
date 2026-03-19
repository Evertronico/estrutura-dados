def busca_sequencial(lista, valor):
    result = -1

    for i, value in enumerate(lista):
        if value == valor:
            result = i
            break
    
    return result

def remover(lista, valor):
    encontrado = busca_sequencial(lista, valor)

    if encontrado == -1:
        return lista
    
    for i in range(encontrado, len(lista) -1):
        lista[i] = lista[i + 1]
    
    del lista[i + 1]

    return lista

lista = [1.0, 5.5, 5.9, 2.3, 4.7, 8.0, 9.5, 7.3, 6.1, 9.9]

print(remover(lista, 2.3))