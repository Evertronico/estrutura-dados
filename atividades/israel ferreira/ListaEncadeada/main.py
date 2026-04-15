from lista_Encadeada import ListaEncadeada

def menu():
    print('=' * 50)
    print('||    <<<<<<<<<<<<MENU DE OPÇÕES>>:>>>>>>>>>    ||')
    print('||    1) -INSERIR INICIO...................:    ||')
    print('||    2) -INSERIR FIM......................:    ||')
    print('||    3) -REMOVER .........................:    ||')
    print('||    4) -EXIBIR...........................:    ||')
    print('||    5) -SAIR.............................:    ||')
    print('=' * 50)

def main():
    lista = ListaEncadeada()

    while True:
        menu()

        opcaoP = input("- ")
        print("-"*50)
        if opcaoP == "1":
            valor = int(input("INSERIR INICIO: "))
            lista.inserir_inicio(valor)
        elif opcaoP == "2":
            valor = int(input("INSERIR FINAL: "))
            lista.inserir_final(valor)
        elif opcaoP == "3":
            valor = int(input("REMOVER VALOR: "))
            lista.remover(valor)
        elif opcaoP == "4":
            print ("Valores na Lista:\n")
            lista.exibir()
            
        elif opcaoP == "5":
                print('Saindo...')
                break
        else:
                print('Opção inválida. Tente novamente')

if __name__ == "__main__":
    main()

