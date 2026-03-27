from listaEncadeada import ListaEncadeada

def menu():
    print("\nMenu:")
    print("1. Inserir no inicio")
    print("2. Inserir no final")
    print("3. Remover elemento")
    print("4. Exibir lista")
    print("0. Sair")

def main():
    lista = ListaEncadeada()

    while True:
        menu()

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            valor =  int(input("Digite o valor: "))
            lista.inserirInicio(valor)
            print("Valor inserido no inicio.")
        
        elif opcao == "2":
            valor =  int(input("Digite o valor: "))
            lista.inserirFim(valor)
            print("Valor inserido no final da lista.")

        elif opcao == "3":
            valor =  int(input("Digite o valor: "))
            lista.remover(valor)
            print("Valor removido com sucesso.")

        elif opcao == "4":
            print("Lista Atual: ")
            lista.exibir()

        elif opcao == "0":
            print("Encerrando...")
            break
    
        else:
            print("Opcao invalida. Tente novamente.")

if __name__ == "__main__":
    main()

