def inserir_ordenado(lista, valor):
    nova_lista = [0] * (len(lista) + 1)

    i = 0
    j = 0
    inserido = False

    while i < len(lista):
        if not inserido and valor < lista[i]:
            nova_lista[j] = valor
            inserido = True
            j += 1
        else:
            nova_lista[j] = lista[i]
            i += 1
            j += 1

    if not inserido:
        nova_lista[j] = valor

    return nova_lista

numeros = []

numeros = inserir_ordenado(numeros, 30)
numeros = inserir_ordenado(numeros, 10)
numeros = inserir_ordenado(numeros, 20)
numeros = inserir_ordenado(numeros, 25)

print("Lista ordenada:", numeros)