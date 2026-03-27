from lista_tarefas import ListaTarefasEncadeada

# Requisito 5: Garantir validação de entrada
def obter_input_valido(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("[Erro] O campo não pode ficar vazio!")

# Requisito 4: Interface via terminal (Menu Interativo)
def iniciar_sistema():
    minha_lista = ListaTarefasEncadeada()
    
    while True:
        print("\n=== GERENCIADOR DE TAREFAS ===")
        print("1. Nova Tarefa (Inserir no Final)")
        print("2. Remover Tarefa (Por Descrição)")
        print("3. Exibir Todas as Tarefas")
        print("4. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            desc = obter_input_valido("Descrição da tarefa: ")
            prio = obter_input_valido("Prioridade (Alta/Média/Baixa): ")
            data = obter_input_valido("Data de criação (ex: 26/03): ")
            minha_lista.inserir_final(desc, prio, data)
            print("[Sucesso] Tarefa adicionada!")

        elif opcao == "2":
            desc_para_remover = input("Digite a descrição da tarefa para remover: ")
            if minha_lista.remover_por_descricao(desc_para_remover):
                print("[Sucesso] Tarefa removida!")
            else:
                print("[Erro] Tarefa não encontrada.")

        elif opcao == "3":
            minha_lista.exibir_lista()

        elif opcao == "4":
            print("Encerrando sistema...")
            break
        else:
            print("[Erro] Opção inválida, tente novamente.")

if __name__ == "__main__":
    iniciar_sistema()