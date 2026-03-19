estoque = []

def buscar_produto(nome):
    for i in range(len(estoque)):
        if estoque[i]["nome"] == nome:
            return i
    return -1

def entrada_produto(nome, quantidade):
    indice = buscar_produto(nome)
    if indice != -1:
        estoque[indice]["quantidade"] += quantidade
        print("Estoque atualizado.")
    else:
        estoque.append({"nome": nome, "quantidade": quantidade})
        print("Produto cadastrado.")

def saida_produto(nome, quantidade):
    indice = buscar_produto(nome)
    if indice != -1:
        if estoque[indice]["quantidade"] >= quantidade:
            estoque[indice]["quantidade"] -= quantidade
            print("Saída realizada.")
        else:
            print("Quantidade insuficiente no estoque.")
    else:
        print("Produto não encontrado.")

def exibir_produtos():
    print("--- Estoque Atual ---")
    for produto in estoque:
        print(f"Produto: {produto['nome']} | Quantidade: {produto['quantidade']}")

entrada_produto("Teclado", 10)
saida_produto("Teclado", 5)
exibir_produtos()