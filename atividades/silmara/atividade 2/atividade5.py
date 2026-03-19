# Exercício 5 – Sistema de Atendimento com Fila
# Implemente um sistema de atendimento para um consultório utilizando lista para simular uma fila de pacientes.
# Requisitos:
#  * Inserir pacientes no final da lista
#  * Remover paciente do início da lista manualmente (sem pop(0))
#  * Implementar função para exibir fila
#  * Controlar caso de fila vazia
#  * Simular múltiplos atendimentos sequenciais

fila = []

def entrar_na_fila(paciente):
    fila.append(paciente)

def atender_paciente():
    if len(fila) == 0:
        print("Fila vazia.")
        return
    
    atendido = fila[0]
    for i in range(len(fila) - 1):
        fila[i] = fila[i+1]
    fila.pop()
    print(f"Atendendo: {atendido}")

def exibir_fila():
    print("Fila atual:", fila)


entrar_na_fila('Lucky')
entrar_na_fila('Felps')
entrar_na_fila('Pompom')
exibir_fila()

atender_paciente()
exibir_fila()