'''
    Exercício 5 – Sistema de Atendimento com Fila
    Implemente um sistema de atendimento para um consultório utilizando lista para simular uma fila de pacientes.
    Requisitos:
    * Inserir pacientes no final da lista
    * Remover paciente do início da lista manualmente (sem pop(0))
    * Implementar função para exibir fila
    * Controlar caso de fila vazia
    * Simular múltiplos atendimentos sequenciais
'''
fila = []

def entrar_na_fila(nome):
    fila.append(nome)
    return f"Paciente {nome} chegou."

def atender_paciente():
    if len(fila) == 0:
        return "A fila está vazia!"
    
    paciente_atendido = fila[0]
    
    # Remover do início manualmente (deslocando elementos)
    for i in range(len(fila) - 1):
        fila[i] = fila[i+1]
    
    del fila[-1] # Remove a duplicata que sobrou no final
    return f"Atendendo agora: {paciente_atendido}"

def exibir_fila():
    if not fila:
        print("Fila vazia.")
    else:
        print("\n--- FILA ATUAL ---")
        for i, paciente in enumerate(fila):
            print(f"{i+1}º - {paciente}")

while True:
    print('=' * 50)
    print('||    <<<<<<<<<<FILA DE CONSULTÓRIO>>>>>>>>>>    ||')
    print('||    1) -NOVO PACIENTE....................:    ||')
    print('||    2) -CHAMAR PRÓXIMO...................:    ||')
    print('||    3) -VISUALIZAR FILA..................:    ||')
    print('||    4) -SAIR.............................:    ||')
    print('=' * 50)

    opcao = input("- ")
    if opcao == "1":
        nome = input("Nome do paciente: ")
        print(entrar_na_fila(nome))
    elif opcao == "2":
        print(atender_paciente())
    elif opcao == "3":
        exibir_fila()
    elif opcao == "4":
        print("Encerrando sistema...")
        break