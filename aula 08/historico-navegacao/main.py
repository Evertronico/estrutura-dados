from historico_navegacao import HistoricoNavegacao

def menu():
    print("\n=== HISTÓRICO DE NAVEGAÇÃO ===")
    print("1 - Visitar site")
    print("2 - Ver histórico")
    print("3 - Apagar site")
    print("0 - Sair")


def main():
    historico = HistoricoNavegacao()

    while True:
        menu()
        opcao = input("Escolha: ")

        if opcao == "1":
            site = input("Digite o site: ")
            historico.visitar(site)

        elif opcao == "2":
            historico.ler()

        elif opcao == "3":
            site = input("Digite o site a remover: ")
            historico.apagar(site)

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()