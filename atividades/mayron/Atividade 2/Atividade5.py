fila = []

def inserir_paciente(nome):
    fila.append(nome)
    print("Paciente", nome, "entrou na fila.")

def atender_paciente():
    if len(fila) == 0:
        print("Fila vazia.")
        return

    paciente_atendido = fila[0]

    for i in range(0, len(fila) - 1):
        fila[i] = fila[i + 1]

    fila.pop()

    print("Paciente atendido:", paciente_atendido)

def exibir_fila():
    print("Fila atual:", fila)

inserir_paciente("Ana")
inserir_paciente("Carlos")
exibir_fila()

atender_paciente()
exibir_fila()