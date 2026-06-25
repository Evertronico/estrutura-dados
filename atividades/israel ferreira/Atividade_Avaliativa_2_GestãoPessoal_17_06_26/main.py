from modulos.agenda import ModuloAgenda
from modulos.projetos import ModuloProjetos
from modulos.financeiro import ModuloFinanceiro
from estruturas.pilha import Pilha

def menu_principal():
    print('=' * 50)
    print('||    <<<<<<<<<<<<<Gestão Pessoal>>>>>>>>>>>>    ||')
    print('||    1) - AGENDA E CONTATOS................:    ||')
    print('||    2) - GESTÃO DE PROJETOS...............:    ||')
    print('||    3) - GESTÃO FINANCEIRA................:    ||')
    print('||    4) - VER HISTÓRICO DE AÇÕES (PILHA)...:    ||')
    print('||    5) - SAIR.............................:    ||')
    print('=' * 50)

def main():
    agenda = ModuloAgenda()
    projetos = ModuloProjetos()
    financeiro = ModuloFinanceiro()
    historico = Pilha()

    while True:
        menu_principal()
        opcao = input("- ")
        
        if opcao == "1":
            historico.empilhar("Acessou Agenda")
            agenda.menu_agenda()
        elif opcao == "2":
            historico.empilhar("Acessou Projetos")
            projetos.menu_projetos()
        elif opcao == "3":
            historico.empilhar("Acessou Financeiro")
            financeiro.menu_financeiro()
        elif opcao == "4":
            print("\n--- Histórico de Ações (Topo da Pilha Primeiro) ---")
            for acao in historico.exibir_historico():
                print(f"-> {acao}")
            input("\nPressione Enter para continuar...")
        elif opcao == "5":
            print('Saindo do sistema...')
            break
        else:
            print('Opção inválida!')

if __name__ == "__main__":
    main()
