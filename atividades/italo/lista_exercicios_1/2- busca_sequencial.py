def busca_sequencial(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1


numeros = [10, 25, 30, 45, 50]

valor_procurado = 30
resultado = busca_sequencial(numeros, valor_procurado)

if resultado != -1:
    print(f"Valor encontrado no índice {resultado}")
else:
    print("Valor não encontrado")