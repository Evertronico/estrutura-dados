from Fila import Fila
from Cliente import Cliente

def menu():
    print("=" * 50)
    print("||    <<<<<<<<<<<<MENU DE ATENDIMENTO BANCÁRIO>>>>>>>>>>    ||")
    print("||    1) - ADICIONAR CLIENTE À FILA........:    ||")
    print("||    2) - ATENDER PRÓXIMO CLIENTE.........:    ||")
    print("||    3) - EXIBIR FILA COMPLETA............:    ||")
    print("||    4) - QUANTIDADE DE CLIENTES AGUARDANDO.:    ||")
    print("||    5) - EXIBIR PRÓXIMO CLIENTE..........:    ||")
    print("||    6) - SAIR............................:    ||")
    print("=" * 50)

def main():
    fila_clientes = Fila()
    id_cliente_counter = 1

    while True:
        menu()
        opcao = input("- ")
        print("-" * 50)

        if opcao == "1":
            nome_cliente = input("Nome do Cliente: ")
            novo_cliente = Cliente(nome_cliente, id_cliente_counter)
            fila_clientes.adicionar_cliente(novo_cliente)
            id_cliente_counter += 1
        elif opcao == "2":
            fila_clientes.atender_cliente()
        elif opcao == "3":
            fila_clientes.exibir_fila_completa()
        elif opcao == "4":
            fila_clientes.quantidade_clientes_aguardando()
        elif opcao == "5":
            fila_clientes.exibir_proximo_cliente()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
        print("\n")

if __name__ == "__main__":
    main()
