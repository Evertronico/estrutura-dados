fila = []

def adicionar_paciente(fila, nome):
    fila.append(nome)

def atender_paciente(fila):
    if len(fila) == 0:
        print("Fila vazia. Nenhum paciente para atender.")
        return None

    paciente_atendido = fila[0]

    nova_fila = []
    for i in range(1, len(fila)):
        nova_fila.append(fila[i])

    fila.clear()
    for paciente in nova_fila:
        fila.append(paciente)

    print(f"Paciente atendido: {paciente_atendido}")
    return paciente_atendido

def exibir_fila(fila):
    if len(fila) == 0:
        print("Fila vazia.")
    else:
        print("Fila de pacientes:")
        for i, paciente in enumerate(fila):
            print(f"{i+1}. {paciente}")


adicionar_paciente(fila, "Ana")
adicionar_paciente(fila, "Carlos")
adicionar_paciente(fila, "Beatriz")
adicionar_paciente(fila, "Daniel")

print("Fila inicial:")
exibir_fila(fila)

print("\nAtendimentos:")
atender_paciente(fila)
atender_paciente(fila)

print("\nFila após atendimentos:")
exibir_fila(fila)

adicionar_paciente(fila, "Eduardo")
print("\nFila após chegada de novo paciente:")
exibir_fila(fila)