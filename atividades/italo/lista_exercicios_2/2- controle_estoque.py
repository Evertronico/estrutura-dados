estoque = []

def buscar_produto(lista, nome):
    for i in range(len(lista)):
        if lista[i]["nome"] == nome:
            return i
    return -1

def entrada_produto(lista, nome, quantidade):
    indice = buscar_produto(lista, nome)

    if indice == -1:
        produto = {"nome": nome, "quantidade": quantidade}
        lista.append(produto)
    else:
        lista[indice]["quantidade"] += quantidade

def saida_produto(lista, nome, quantidade):
    indice = buscar_produto(lista, nome)

    if indice == -1:
        print("Produto não encontrado.")
        return

    if lista[indice]["quantidade"] < quantidade:
        print("Estoque insuficiente.")
        return

    lista[indice]["quantidade"] -= quantidade

def exibir_estoque(lista):
    if len(lista) == 0:
        print("Estoque vazio.")
    else:
        print("Estoque:")
        for produto in lista:
            print(f'Produto: {produto["nome"]} | Quantidade: {produto["quantidade"]}')

entrada_produto(estoque, "Arroz", 10)
entrada_produto(estoque, "Feijão", 5)
entrada_produto(estoque, "Arroz", 5)

exibir_estoque(estoque)

print("\nSaída de produtos:")
saida_produto(estoque, "Arroz", 8)
saida_produto(estoque, "Feijão", 10)

exibir_estoque(estoque)