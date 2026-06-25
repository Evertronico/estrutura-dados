from caregar import carregar_solicitacoes
from fila_prioridade import FilaPrioridade
from atualizar_status import concluir_solicitacao

def main():
    fila = None

    while True:
        print("\n===== MENU DA FILA DE SAÚDE =====")
        print("1. Carregar/Recarregar Fila")
        print("2. Exibir Fila Atual")
        print("3. Atender Próximo Paciente")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("Carregando solicitações...")
            solicitacoes = carregar_solicitacoes()
            fila = FilaPrioridade(solicitacoes)
            print("Fila carregada com sucesso!")
        elif opcao == '2':
            if fila:
                fila.exibir()
            else:
                print("A fila não foi carregada. Por favor, carregue a fila primeiro.")
        elif opcao == '3':
            if fila:
                paciente_atendido = fila.atender()
                if paciente_atendido:
                    print(f"Atendendo paciente: {paciente_atendido.paciente} (ID: {paciente_atendido.id})")
                    concluir_solicitacao(paciente_atendido.id)
                    print("Status do paciente atualizado para CONCLUIDO no banco de dados.")
                else:
                    print("Não há pacientes na fila para atender.")
            else:
                print("A fila não foi carregada. Por favor, carregue a fila primeiro.")
        elif opcao == '4':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

