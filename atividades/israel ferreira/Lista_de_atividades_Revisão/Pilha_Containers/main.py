from Pilha import Pilha
from Container import Container

def menu():
    print("=" * 50)
    print("||    <<<<<<<<<<<<MENU DE CONTROLE DE CONTAINERS>>>>>>>>>>    ||")
    print("||    1) - EMPILHAR CONTAINER..............:    ||")
    print("||    2) - DESEMPILHAR CONTAINER...........:    ||")
    print("||    3) - EXIBIR CONTAINER DO TOPO........:    ||")
    print("||    4) - EXIBIR TODOS OS CONTAINERS......:    ||")
    print("||    5) - QUANTIDADE ARMAZENADA...........:    ||")
    print("||    6) - SAIR............................:    ||")
    print("=" * 50)

def main():
    pilha_containers = Pilha()

    while True:
        menu()
        opcao = input("- ")
        print("-" * 50)

        if opcao == "1":
            id_container = input("ID do Container para empilhar: ")
            novo_container = Container(id_container)
            pilha_containers.empilhar(novo_container)
        elif opcao == "2":
            pilha_containers.desempilhar()
        elif opcao == "3":
            pilha_containers.exibir_topo()
        elif opcao == "4":
            pilha_containers.exibir_todos()
        elif opcao == "5":
            pilha_containers.quantidade_armazenada()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
        print("\n")

if __name__ == "__main__":
    main()
