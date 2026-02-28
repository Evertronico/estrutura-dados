produtos = []

def menu():
    print("------------------------------------------------------------------")
    print("Digite 1 para cadastrar um produto")
    print("Digite 2 para listar os produtos cadastrados")
    print("Digite 3 para deletar um produto")
    print("Digite 4 para sair do sistema")
    return int(input("Digite a opção desejada: "))

while True:
    opcao = menu()

    if opcao == 1:
        produto = input("Digite o nome do produto: ")
        produtos.append(produto)
        print("Produto cadastrado com sucesso!")

    elif opcao == 2:
        print("------------------------------------------------------------------")
        print("Produtos cadastrados:")
        print("------------------------------------------------------------------")

        for produto in produtos:
            print(produto)

    elif opcao == 3:
        produto = input("Digite o nome do produto que deseja deletar: ")
        if produto in produtos:
            produtos.remove(produto)
            print("Produto deletado com sucesso!")
        else:
            print("Produto não encontrado!")

    elif opcao == 4:
        print("Saindo do sistema...")
        break  

    else:
        print("Opção inválida! Tente novamente.")
