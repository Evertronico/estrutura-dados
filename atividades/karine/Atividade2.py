notas = [3, 6.9, 8.5, 9.9, 7, 10, 3.6, 9, 1.1, 2]

def busca_sequencial(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1

valor_procurado = 10

resultado = busca_sequencial(notas, valor_procurado)

if resultado != -1:
    print(f"O valor {valor_procurado} foi encontrado no índice: {resultado}")
else:
    print(f"O valor {valor_procurado} não está na lista.")