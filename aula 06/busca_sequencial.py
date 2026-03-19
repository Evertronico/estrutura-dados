def busca_sequencial(lista, valor):
    # Percorre a lista elemento por elemento
    for i in range(len(lista)):
        if lista[i] == valor:
            return i  # Retorna índice se encontrar
    return -1  # Valor sentinela caso não exista

dados = [10, 25, 30, 45, 50]
print("Índice encontrado:", busca_sequencial(dados, 30))