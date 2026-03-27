# Lista que vai armazenar os produtos
# Cada produto será um dicionário: {"nome": "Produto", "quantidade": 10}
estoque = []

# Função para buscar um produto pelo nome (sem usar 'in')
def buscar_produto(nome):
    for i in range(len(estoque)):
        if estoque[i]["nome"] == nome:
            return i  # retorna a posição do produto
    return -1  # não encontrou

# Função para adicionar ou atualizar produto
def entrada_produto(nome, quantidade):
    posicao = buscar_produto(nome)
    
    if posicao != -1:
        # Produto já existe → só soma a quantidade
        estoque[posicao]["quantidade"] += quantidade
        print(f"Quantidade atualizada! Agora temos {estoque[posicao]['quantidade']} unidades de '{nome}'.")
    else:
        # Produto não existe → cria novo
        produto = {"nome": nome, "quantidade": quantidade}
        estoque.append(produto)
        print(f"Produto '{nome}' adicionado ao estoque!")

# Função para saída de produto
def saida_produto(nome, quantidade):
    posicao = buscar_produto(nome)
    
    if posicao == -1:
        print("Produto não encontrado.")
        return
    
    # Verifica se tem quantidade suficiente
    if quantidade > estoque[posicao]["quantidade"]:
        print("Erro: quantidade solicitada maior que o estoque disponível!")
        return
    
    # Faz a retirada
    estoque[posicao]["quantidade"] -= quantidade
    print(f"Saída realizada! Restam {estoque[posicao]['quantidade']} unidades de '{nome}'.")

# Função para exibir todos os produtos
def listar_produtos():
    if len(estoque) == 0:
        print("Estoque vazio.")
        return
    
    print("\n=== ESTOQUE ===")
    for i in range(len(estoque)):
        print(f"{i+1} - {estoque[i]['nome']} | Quantidade: {estoque[i]['quantidade']}")

# -------------------------
# MENU INTERATIVO
# -------------------------

while True:
    print("\n===== MENU ESTOQUE =====")
    print("1 - Entrada de produto")
    print("2 - Saída de produto")
    print("3 - Buscar produto")
    print("4 - Listar produtos")
    print("0 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    # Entrada (adicionar ou atualizar)
    if opcao == "1":
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade: "))
        entrada_produto(nome, quantidade)
    
    # Saída
    elif opcao == "2":
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade: "))
        saida_produto(nome, quantidade)
    
    # Busca
    elif opcao == "3":
        nome = input("Nome do produto: ")
        posicao = buscar_produto(nome)
        
        if posicao != -1:
            print(f"Produto encontrado: {estoque[posicao]['nome']} | Quantidade: {estoque[posicao]['quantidade']}")
        else:
            print("Produto não encontrado.")
    
    # Listar
    elif opcao == "4":
        listar_produtos()
    
    # Sair
    elif opcao == "0":
        print("Encerrando sistema... 👋")
        break
    
    else:
        print("Opção inválida, tenta de novo!")