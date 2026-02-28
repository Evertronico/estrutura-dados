produtos = []

def menu():
    print("------------------------------------------------------------------")
    print("Digite 1 para cadastrar um produto")
    print("Digite 2 para listar os produtos cadastrados")
    print("Digite 3 para deletar um produto pelo nome")
    print("Digite 4 para calcular o valor total do estoque")
    print("Digite 5 para sair do sistema")
    return int(input("Digite a opção desejada: "))

while True:
    opcao = menu()

    if opcao == 1:
        nome = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade: "))
        preco = float(input("Digite o preço unitário: "))
        
        produto = {"nome": nome, "quantidade": quantidade, "preco": preco}
        produtos.append(produto)
        print("Produto cadastrado com sucesso!")

    elif opcao == 2:
        print("------------------------------------------------------------------")
        print("Produtos cadastrados:")
        print("------------------------------------------------------------------")
        if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            for p in produtos:
                print(f"Nome: {p['nome']} | Quantidade: {p['quantidade']} | Preço: R${p['preco']:.2f}")

    elif opcao == 3:
        nome = input("Digite o nome do produto que deseja deletar: ")
        encontrado = False
        for p in produtos:
            if p["nome"].lower() == nome.lower():
                produtos.remove(p)
                print("Produto deletado com sucesso!")
                encontrado = True
                break
        if not encontrado:
            print("Produto não encontrado!")

    elif opcao == 4:
        total = sum(p["quantidade"] * p["preco"] for p in produtos)
        print(f"Valor total do estoque: R${total:.2f}")

    elif opcao == 5:
        print("Saindo do sistema...")
        break  

    else:
        print("Opção inválida! Tente novamente.")
