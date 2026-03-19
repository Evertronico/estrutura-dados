def inserirordenado(lista, valor):
    lista.append(0)
    
    i = len(lista) - 2
    
    # procura a posição pra inserir o valor
    while i >= 0 and lista[i] > valor:
        lista[i + 1] = lista[i]
        i = i - 1
        
    lista [i + 1] = lista[i]
    lista[i + 1] = valor
    
    return lista

lista = [1, 2, 5, 6, 7]
inserirordenado(lista, 3)
inserirordenado(lista, 4)


print(lista)