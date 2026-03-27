from historicoNavegacao import HistoricoNavegacao

def menu():
    print("\nMenu:")
    print("1. Visitar o site")
    print("2. Ver historico")
    print("3. Apagar site no historico")
    print("4. Sair")

def main():
    historico = HistoricoNavegacao()

    while True:
        menu()

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            site =  input("Digite o site: ")
            historico.visitar(site)

        elif opcao == "2":
            historico.ler()

        elif opcao == "3":
            site =  input("Digite o site: ")
            historico.apagar(site)

        elif opcao == "4":
            print("Saido...")
            break
    
        else:
            print("Opcao invalida. Tente novamente.")

if __name__ == "__main__":
    main()

