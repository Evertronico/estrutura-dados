from historico_navegacao import HistoricoNavegacao

def menu():
    print("\nMenu:")
    print("1. Visitar site")
    print("2. Ver histórico")
    print("3. Apagar site do histórico")
    print("4. Sair")

def main():
    historico = HistoricoNavegacao()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            site = input("Digite a URL do site: ")
            historico.visitar(site)
        elif opcao == '2':
            historico.ler()
        elif opcao == '3':
            site = input("Digite a URL do site a ser apagado: ")
            historico.apagar(site)
        elif opcao  == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
if __name__ == "__main__":
    main()