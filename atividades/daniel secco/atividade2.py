def busca_sequencial(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1
# pega o valor e retorna a posição


valores = [10, 13, 55, 1009, 108]
busca = busca_sequencial(valores, 55)

print(busca)