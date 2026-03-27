'''
        Exercício 2 – Controle de Estoque com Validação de Regras
    Implemente um sistema de controle de estoque para uma loja. Cada produto deve possuir nome e quantidade disponível.
    Requisitos:
    Utilizar lista de estruturas (dicionário ou lista composta)
    * Implementar entrada de produto (adicionar ou atualizar quantidade)
    * Implementar saída de produto com validação de estoque
    * Impedir retirada maior que a quantidade disponível
    * Implementar busca de produto pelo nome
    * Exibir todos os produtos

'''

estoque = []

def entrada_produto(nome, quantidade):
    for produto in estoque:
        if produto["nome"].lower() == nome.lower():
            produto["quantidade"] += quantidade
            return f"Quantidade de {nome} atualizada para {produto['quantidade']}."
    novo = {"nome": nome, "quantidade": quantidade}
    estoque.append(novo)
    return f"Produto {nome} adicionado com {quantidade} unidades."

def saida_produto(nome, quantidade):
    for produto in estoque:
        if produto["nome"].lower() == nome.lower():
            if quantidade <= produto["quantidade"]:
                produto["quantidade"] -= quantidade
                return f"{quantidade} unidades de {nome} retiradas. Restam {produto['quantidade']}."
            else:
                return f"Estoque insuficiente de {nome}. Disponível: {produto['quantidade']}."
    return f"{nome} não encontrado no estoque."

def busca_produto(nome):
    for produto in estoque:
        if produto["nome"].lower() == nome.lower():
            return f"{nome} encontrado com {produto['quantidade']} unidades."
    return f"{nome} não está no estoque."

def listar_produtos():
    if len(estoque) == 0:
        return ["Não há produtos cadastrados."]
    return estoque[:]

# Menu interativo
while True:
    print('=' * 50)
    print('||    <<<<<<<<<<<MENU DE ESTOQUE>>>>>>>>>>>    ||')
    print('||    1) -ENTRADA DE PRODUTO...............:    ||')
    print('||    2) -SAÍDA DE PRODUTO.................:    ||')
    print('||    3) -BUSCAR PRODUTO...................:    ||')
    print('||    4) -LISTAR PRODUTOS..................:    ||')
    print('||    5) -SAIR.............................:    ||')
    print('=' * 50)

    opcao = input("- ")
    print("-"*50)

    if opcao == "1":
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade: "))
        print(entrada_produto(nome, quantidade))

    elif opcao == "2":
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade a retirar: "))
        print(saida_produto(nome, quantidade))

    elif opcao == "3":
        nome = input("Nome do produto: ")
        print(busca_produto(nome))

    elif opcao == "4":
        produtos = listar_produtos()
        for p in produtos:
            print(p)

    elif opcao == "5":
        print("Saindo do sistema de estoque...")
        break

    else:
        print("Opção inválida. Tente novamente.")