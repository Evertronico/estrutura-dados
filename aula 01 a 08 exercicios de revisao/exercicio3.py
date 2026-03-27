def inserir_ordenado(lista, valor):
    lista.append(valor)  # cria espaço

    i = len(lista) - 2

    # desloca elementos maiores
    while i >= 0 and lista[i] > valor:
        lista[i + 1] = lista[i]
        i -= 1

    lista[i + 1] = valor


# Teste
lista = [10, 20, 30, 40]

inserir_ordenado(lista, 25)
inserir_ordenado(lista, 5)

print(lista)