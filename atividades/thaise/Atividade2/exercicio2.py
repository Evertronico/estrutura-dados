# Lista de produtos (cada produto é um dicionário)
estoque = []


# Buscar produto pelo nome (sem usar in ou index)
def buscar_produto(lista, nome):
    for i in range(len(lista)):
        if lista[i]["nome"] == nome:
            return i
    return -1


# Entrada de produto (adicionar ou atualizar)
def entrada_produto(lista, nome, quantidade):
    pos = buscar_produto(lista, nome)

    if pos != -1:
        lista[pos]["quantidade"] += quantidade
        print(f"Quantidade atualizada! Novo estoque: {lista[pos]['quantidade']}")
    else:
        produto = {"nome": nome, "quantidade": quantidade}
        lista.append(produto)
        print("Produto cadastrado com sucesso!")


# Saída de produto (com validação)
def saida_produto(lista, nome, quantidade):
    pos = buscar_produto(lista, nome)

    if pos == -1:
        print("Produto não encontrado!")
        return

    if lista[pos]["quantidade"] < quantidade:
        print("❌ Estoque insuficiente!")
        return

    lista[pos]["quantidade"] -= quantidade
    print(f"Saída realizada! Estoque atual: {lista[pos]['quantidade']}")


# Exibir produtos
def exibir_produtos(lista):
    print("\n📦 Estoque:")
    if len(lista) == 0:
        print("Nenhum produto cadastrado.")
    else:
        for i in range(len(lista)):
            print(f"{i} - {lista[i]['nome']} | Quantidade: {lista[i]['quantidade']}")


# MENU
while True:
    print("\n===== CONTROLE DE ESTOQUE =====")
    print("1 - Entrada de produto")
    print("2 - Saída de produto")
    print("3 - Buscar produto")
    print("4 - Exibir estoque")
    print("0 - Sair")

    opcao = input("Digite a opção: ")

    if opcao == "1":
        print("\n--- Entrada de Produto ---")
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade: "))
        entrada_produto(estoque, nome, quantidade)

    elif opcao == "2":
        print("\n--- Saída de Produto ---")
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade a retirar: "))
        saida_produto(estoque, nome, quantidade)

    elif opcao == "3":
        print("\n--- Buscar Produto ---")
        nome = input("Nome do produto: ")
        pos = buscar_produto(estoque, nome)

        if pos != -1:
            print(f"Produto encontrado: {estoque[pos]['nome']} | Quantidade: {estoque[pos]['quantidade']}")
        else:
            print("Produto não encontrado!")

    elif opcao == "4":
        exibir_produtos(estoque)

    elif opcao == "0":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")