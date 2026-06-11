from ListaTarefas import ListaTarefas
from Tarefa import Tarefa

def menu():
    print("=" * 50)
    print("||    <<<<<<<<<<<<MENU DE GERENCIAMENTO DE TAREFAS>>>>>>>>>>    ||")
    print("||    1) - INSERIR TAREFA..................:    ||")
    print("||    2) - BUSCAR TAREFA...................:    ||")
    print("||    3) - REMOVER TAREFA CONCLUÍDA........:    ||")
    print("||    4) - EXIBIR TAREFAS PENDENTES........:    ||")
    print("||    5) - QUANTIDADE DE TAREFAS...........:    ||")
    print("||    6) - SAIR............................:    ||")
    print("=" * 50)

def main():
    lista_tarefas = ListaTarefas()

    while True:
        menu()
        opcao = input("- ")
        print("-" * 50)

        if opcao == "1":
            descricao = input("Descrição da Tarefa: ")
            nova_tarefa = Tarefa(descricao)
            lista_tarefas.inserir_final(nova_tarefa)
            print(f"Tarefa \'{descricao}\' inserida com sucesso!")
        elif opcao == "2":
            descricao = input("Descrição da Tarefa para buscar: ")
            tarefa_encontrada = lista_tarefas.buscar_tarefa(descricao)
            if tarefa_encontrada:
                print("Tarefa encontrada:")
                print(tarefa_encontrada)
            else:
                print(f"Tarefa com descrição \'{descricao}\' não encontrada.")
        elif opcao == "3":
            descricao = input("Descrição da Tarefa concluída para remover: ")
            if lista_tarefas.remover_tarefa(descricao):
                print(f"Tarefa \'{descricao}\' removida com sucesso!")
            else:
                print(f"Tarefa com descrição \'{descricao}\' não encontrada.")
        elif opcao == "4":
            lista_tarefas.exibir_tarefas_pendentes()
        elif opcao == "5":
            print(f"Quantidade de tarefas cadastradas: {lista_tarefas.quantidade_tarefas()}")
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
        print("\n")

if __name__ == "__main__":
    main()
