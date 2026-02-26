estoque = []

def inserir_produto():
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    preco = float(input("Digite o preço unitário: "))
    
    produto = {
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }

    estoque.append(produto)
    
    print("Produto inserido com sucesso!\n")

def remover_produto():
    nome = input("Digite o nome do produto a remover: ")
    
    for produto in estoque:
        if produto["nome"].lower() == nome.lower():
            estoque.remove(produto)
            print("Produto removido com sucesso!\n")
            return
    
    print("Produto não encontrado.\n")

def listar_produtos():
    if not estoque:
        print("Estoque vazio.\n")
        return
    
    print("\n=== LISTA DE PRODUTOS ===")
    for produto in estoque:
        print(f"Nome: {produto['nome']}")
        print(f"Quantidade: {produto['quantidade']}")
        print(f"Preço: R$ {produto['preco']:.2f}")
        print("------------------------")
    print()

def calcular_total():
    total = 0
    
    for produto in estoque:
        total += produto["quantidade"] * produto["preco"]
    
    print(f"\nValor total do estoque: R$ {total:.2f}\n")

def menu():
    while True:
        print("===== MENU ESTOQUE =====")
        print("1 - Inserir produto")
        print("2 - Remover produto")
        print("3 - Listar produtos")
        print("4 - Calcular valor total")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            inserir_produto()
        elif opcao == "2":
            remover_produto()
        elif opcao == "3":
            listar_produtos()
        elif opcao == "4":
            calcular_total()
        elif opcao == "0":
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida.\n")

menu()