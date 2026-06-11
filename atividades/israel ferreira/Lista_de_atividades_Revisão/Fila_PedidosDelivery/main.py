from Fila import Fila
from Pedido import Pedido

def menu():
    print("=" * 50)
    print("||    <<<<<<<<<<<<MENU DE PROCESSAMENTO DE PEDIDOS>>>>>>>>>>    ||")
    print("||    1) - REGISTRAR NOVO PEDIDO...........:    ||")
    print("||    2) - PROCESSAR PRÓXIMO PEDIDO........:    ||")
    print("||    3) - EXIBIR FILA DE PEDIDOS PENDENTES:    ||")
    print("||    4) - CONSULTAR PRÓXIMO PEDIDO........:    ||")
    print("||    5) - QUANTIDADE DE PEDIDOS AGUARDANDO:    ||")
    print("||    6) - SAIR............................:    ||")
    print("=" * 50)

def main():
    fila_pedidos = Fila()
    id_pedido_counter = 1

    while True:
        menu()
        opcao = input("- ")
        print("-" * 50)

        if opcao == "1":
            descricao_pedido = input("Descrição do Pedido: ")
            novo_pedido = Pedido(id_pedido_counter, descricao_pedido)
            fila_pedidos.registrar_pedido(novo_pedido)
            id_pedido_counter += 1
        elif opcao == "2":
            fila_pedidos.processar_proximo_pedido()
        elif opcao == "3":
            fila_pedidos.exibir_pedidos_pendentes()
        elif opcao == "4":
            fila_pedidos.consultar_proximo_pedido()
        elif opcao == "5":
            fila_pedidos.quantidade_pedidos_aguardando()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
        print("\n")

if __name__ == "__main__":
    main()
