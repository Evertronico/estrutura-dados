fila = []

# chegada de clientes
fila.append("Ana")
fila.append("Carlos")
fila.append("Marina")

print("Fila atual:", fila)

# atendimento
cliente_atendido = fila.pop(0)

print("Cliente atendido:", cliente_atendido)
print("Fila após atendimento:", fila)