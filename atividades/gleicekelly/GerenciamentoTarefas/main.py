from gerenciamentoTarefas import GerenciamentoTarefas

def menu():
    print("\nMenu:")
    print("1. Cadastrar Tarefa")
    print("2. Ver Tarefa")
    print("3. Apagar Tarefa")
    print("4. Sair")

def main():
    tarefa = GerenciamentoTarefas()

    while True:
        menu()

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            desc = input("Descrição: ")
            prio = input("Prioridade: ")
            tarefa.gravarTarefa(desc, prio)

        elif opcao == "2":
            tarefa.exibir()

        elif opcao == "3":
            tarefas = input("Digite a tarefa: ")
            tarefa.remover(tarefas)

        elif opcao == "4":
            print("Saido...")
            break
    
        else:
            print("Opcao invalida. Tente novamente.")

if __name__ == "__main__":
    main()

