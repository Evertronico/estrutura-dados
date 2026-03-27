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
        print("Novo produto cadastrado.")

def saida_produto(nome, quantidade):
    indice = buscar_produto(nome)
    if indice != -1:
        if estoque[indice]["quantidade"] >= quantidade:
            estoque[indice]["quantidade"] -= quantidade
            print("Saída realizada com sucesso.")
        else:
            print("Erro: Estoque insuficiente!")
    else:
        print("Produto não localizado.")

def exibir_produtos():
    print("--- Estoque Atual ---")
    for i in range(len(estoque)):
        print(f"Produto: {estoque[i]['nome']} | Quantidade: {estoque[i]['quantidade']}")

entrada_produto("Teclado", 10)
entrada_produto("Mouse", 5)
saida_produto("Teclado", 3)
saida_produto("Mouse", 10)
exibir_produtos()