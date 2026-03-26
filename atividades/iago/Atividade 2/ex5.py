# Atividade 2 - Ex 5: Fila de Espera
fila = ["Paciente 1", "Paciente 2", "Paciente 3"]

def proximo_atendimento(lista):
    if len(lista) == 0:
        print("Fila vazia!")
        return
    
    atendido = lista[0]
    # Desloca todos para a esquerda (quem era 2º vira 1º)
    for i in range(len(lista) - 1):
        lista[i] = lista[i+1]
    
    lista[:] = lista[:-1]
    print(f"A atender agora: {atendido}")

# Teste
proximo_atendimento(fila)
print(f"Próximos na fila: {fila}")