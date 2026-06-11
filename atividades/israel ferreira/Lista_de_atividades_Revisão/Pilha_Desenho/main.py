from Pilha import Pilha
from Acao import Acao

def menu():
    print("=" * 50)
    print("||    <<<<<<<<<<<<MENU DE DESFAZER OPERAÇÕES>>>>>>>>>>    ||")
    print("||    1) - REGISTRAR NOVA AÇÃO.............:    ||")
    print("||    2) - DESFAZER ÚLTIMA AÇÃO............:    ||")
    print("||    3) - EXIBIR HISTÓRICO DE AÇÕES.......:    ||")
    print("||    4) - MOSTRAR ÚLTIMA AÇÃO REALIZADA...:    ||")
    print("||    5) - SAIR............................:    ||")
    print("=" * 50)

def main():
    pilha_acoes = Pilha()

    while True:
        menu()
        opcao = input("- ")
        print("-" * 50)

        if opcao == "1":
            descricao_acao = input("Descrição da nova ação: ")
            nova_acao = Acao(descricao_acao)
            pilha_acoes.empilhar(nova_acao)
            print(f"Ação \'{descricao_acao}\' registrada com sucesso!")
        elif opcao == "2":
            acao_desfeita = pilha_acoes.desempilhar()
            if acao_desfeita:
                print(f"Ação desfeita: {acao_desfeita.descricao}")
            else:
                print("Pilha de ações vazia. Nada para desfazer.")
        elif opcao == "3":
            pilha_acoes.exibir_historico()
        elif opcao == "4":
            ultima_acao = pilha_acoes.mostrar_ultima_acao()
            if ultima_acao:
                print(f"Última ação realizada: {ultima_acao.descricao}")
            else:
                print("Pilha de ações vazia. Nenhuma ação realizada.")
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
        print("\n")

if __name__ == "__main__":
    main()
