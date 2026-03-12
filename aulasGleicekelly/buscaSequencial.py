#função que busca sequencial
def busca_sequencial(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1
    
notas = [2.0, 5.0, 9.5, 6.0, 6.1, 7.2, 3.0, 6.8]
print("Indice encontrado: ", busca_sequencial(notas, 7.2))