estoque = []

def inserir_produto(nome, quantidade, preco):
    produto = {"nome": nome, "quantidade": quantidade, "preco": preco}
    estoque.append(produto)
    print(f"Produto '{nome}' adicionado com sucesso!")

def remover_produto(nome_produto):
    for i, produto in enumerate(estoque):
        if produto["nome"].lower() == nome_produto.lower():
            del estoque[i]
            print(f"Produto '{nome_produto}' removido do estoque.")
            return 
    
    print(f"Produto '{nome_produto}' não encontrado.")

def listar_produtos():
    if not estoque:
        print("O estoque está vazio no momento.")
        return

    print("--- Lista de Produtos no Estoque ---")
    for produto in estoque:
        print(f"Nome: {produto['nome']} | Quant.: {produto['quantidade']} | Preço: {produto['preco']:.2f}€")
    print("------------------------------------")

def calcular_total_estoque():
    soma_total = 0 
    for produto in estoque:
        soma_total += produto["quantidade"] * produto["preco"]
        
    print(f"Valor total do estoque: {soma_total:.2f}€")

while True:
    print("==============================")
    print("1 - Inserir novo produto")
    print("2 - Remover produto")
    print("3 - Listar todos os produtos")
    print("4 - Calcular valor total")
    print("0 - Sair do programa")
    print("==============================")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        nome_input = input("Digite o nome do produto: ")
        qtd_input = int(input("Digite a quantidade: "))
        preco_input = float(input("Digite o preço unitário: "))
        inserir_produto(nome_input, qtd_input, preco_input)
        
    elif opcao == '2':
        nome_remover = input("Digite o nome do produto que deseja remover: ")
        remover_produto(nome_remover)
        
    elif opcao == '3':
        listar_produtos()
        
    elif opcao == '4':
        calcular_total_estoque()
        
    elif opcao == '0':
        print("A sair do sistema...")
        break
        
    else:
        print("Opção inválida! Por favor, digite um número do menu.")