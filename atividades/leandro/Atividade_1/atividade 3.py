def remover(lista, valor):
    indice = -1
    
    #localizar o elemento
    for i in range(len(lista)):
        if lista[i] == valor:
            indice = i
            break
    
    if indice == -1:
        print("Valor não encontrado")
        return lista
    
    #deslocar elementos para a esquerda
    for i in range(indice, len(lista) - 1):
        lista[i] = lista[i + 1]
    
    #atualizar a lista e remover último duplicado
    lista = lista[:-1]
    
    return lista


numeros = [10, 20, 30, 40, 50]

numeros = remover(numeros, 30)

print(numeros)