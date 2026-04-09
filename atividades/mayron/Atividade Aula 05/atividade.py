def calcular_novo_preco(preco):
    return preco * 1.10

def exibir_resultado(nome, novo_preco):
    print("Produto:", nome)
    print("Novo preço:", novo_preco)

nome = input("Nome do produto: ")
preco = float(input("Preço: "))

novo_preco = calcular_novo_preco(preco)
exibir_resultado(nome, novo_preco)