# lista de dados (estrutura linear)
dados = [10, 20, 30, 40, 50]

# valor da busca
valor = int(input("Digite o valor a ser buscado: "))

# função de busca sequencial (TDA simplificado)
def busca(lista, valor):
    # percorre a lista com indices
    for i in range(len(lista)):
        # comparação elemento a elemento
        if lista[i] == valor:
            return i # retorna a posição
    # caso o valor não seja encontrado na lista
    return -1

# realiza a chamada da função
resultado = busca(dados, valor)

# exibe o resultado da busca
if resultado != -1:
    print(f"Valor encontrado na posição: {resultado}")
else:
    print("Valor não encontrado na lista.")