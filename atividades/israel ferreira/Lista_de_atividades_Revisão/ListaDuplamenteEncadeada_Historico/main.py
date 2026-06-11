from HistoricoEdicao import HistoricoEdicao

def menu():
    print("=" * 50)
    print("||    <<<<<<<<<<<<MENU DE HISTÓRICO DE EDIÇÃO>>>>>>>>>>    ||")
    print("||    1) - ADICIONAR NOVA VERSÃO.............:    ||")
    print("||    2) - AVANÇAR PARA VERSÃO MAIS RECENTE..:    ||")
    print("||    3) - RETORNAR PARA VERSÃO ANTERIOR.....:    ||")
    print("||    4) - EXIBIR VERSÃO ATUAL...............:    ||")
    print("||    5) - EXIBIR TODO O HISTÓRICO...........:    ||")
    print("||    6) - SAIR............................:    ||")
    print("=" * 50)

def main():
    historico = HistoricoEdicao()

    while True:
        menu()
        opcao = input("- ")
        print("-" * 50)

        if opcao == "1":
            descricao = input("Descrição da alteração para a nova versão: ")
            historico.adicionar_versao(descricao)
            print(f"Nova versão \'{descricao}\' adicionada com sucesso!")
        elif opcao == "2":
            if historico.avancar_versao():
                print("Avançou para a versão mais recente.")
            else:
                print("Não há versões mais recentes.")
        elif opcao == "3":
            if historico.retornar_versao():
                print("Retornou para a versão anterior.")
            else:
                print("Não há versões anteriores.")
        elif opcao == "4":
            print(historico.exibir_versao_atual())
        elif opcao == "5":
            historico.exibir_historico()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
        print("\n")

if __name__ == "__main__":
    main()
