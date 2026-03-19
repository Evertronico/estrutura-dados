def sistema_fila():
    fila = []

    def adicionar_paciente(nome):
        fila.append(nome)
        print(f"Paciente '{nome}' entrou na fila.")

    def atender_paciente():
        if not fila:
            print("Aviso: A fila está vazia. Ninguém para atender.")
            return None

        paciente_atendido = fila[0]

        for i in range(1, len(fila)):
            fila[i - 1] = fila[i]
        
        fila.pop()

        print(f"Atendendo agora: {paciente_atendido}")
        return paciente_atendido

    def exibir_fila():
        if not fila:
            print("Nenhum paciente na fila.")
        else:
            for i, paciente in enumerate(fila, start=1):
                print(f"{i}º - {paciente}")

    adicionar_paciente("Ana")
    adicionar_paciente("Bruno")
    adicionar_paciente("Carlos")
    
    exibir_fila()
    
    atender_paciente() 
    exibir_fila()
    
    atender_paciente() 
    atender_paciente() 
    atender_paciente()

sistema_fila()