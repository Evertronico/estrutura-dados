fila = []

# registra a ordem de chegada das pessoas

fila.append("Joao")
fila.append("Maria")
fila.append("Pedro")

print("Fila inicial:", fila)

# realiza o atendimento da primeira pessoa na fila
clienteAtendido = fila.pop(0)

print("Clientes atendidos: ", clienteAtendido)
print("Fila restante: ", fila)