from lista_encadeada import ListaEncadeada

def menu():
    print("\n=== MENU ===")
    print("1 - Inserir no início")
    print("2 - Inserir no final")
    print("3 - Remover elemento")
    print("4 - Exibir lista")
    print("0 - Sair")

def main():
    lista = ListaEncadeada()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = int(input("Digite o valor: "))
            lista.inserir_inicio(valor)
            print("Valor inserido no início.")

        elif opcao == "2":
            valor = int(input("Digite o valor: "))
            lista.inserir_final(valor)
            print("Valor inserido no final.")

        elif opcao == "3":
            valor = int(input("Digite o valor a remover: "))
            lista.remover(valor)
            print("Operação de remoção executada.")

        elif opcao == "4":
            print("\nLista atual:")
            lista.exibir()

        elif opcao == "0":
            print("Encerrando...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()