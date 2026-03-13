dados = [10, 25, 30, 45, 50]

def busca_sequencial(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i 
    return -1  

print("Índice encontrado:", busca_sequencial(dados, 30))
print("Índice encontrado:", busca_sequencial(dados, 99))