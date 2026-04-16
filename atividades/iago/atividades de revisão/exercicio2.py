# Lista de dados (estrutura linear)
dados = [10, 20, 30, 40, 50]

# Valor a buscar
valor = int(input("Digite o valor a buscar: "))

# Função de busca sequencial (TDA simplificado)
def busca(lista, valor):
    # Percorre a lista com índice
    for i in range(len(lista)):
        # Comparação elemento a elemento
        if lista[i] == valor:
            return i # retorna posição
    return -1 # não encontrado

# Chamada da função
resultado = busca(dados, valor)

# Saída
if resultado != -1:
    print("Encontrado na posição:", resultado)
else:
    print("Valor não encontrado")