def buscar_produto(estoque, nome):
    for i in range(len(estoque)):
        if estoque[i]["nome"] == nome:
            return i
    return -1


def entrada(estoque, nome, quantidade):
    pos = buscar_produto(estoque, nome)

    if pos == -1:
        estoque.append({"nome": nome, "quantidade": quantidade})
    else:
        estoque[pos]["quantidade"] += quantidade


def saida(estoque, nome, quantidade):
    pos = buscar_produto(estoque, nome)

    if pos == -1:
        print("Produto não encontrado.")
        return

    if estoque[pos]["quantidade"] < quantidade:
        print("Estoque insuficiente.")
        return

    estoque[pos]["quantidade"] -= quantidade


def exibir(estoque):
    for produto in estoque:
        print(produto["nome"], "-", produto["quantidade"])


# Teste
estoque = []

entrada(estoque, "Mouse", 10)
entrada(estoque, "Teclado", 5)
saida(estoque, "Mouse", 3)

exibir(estoque)