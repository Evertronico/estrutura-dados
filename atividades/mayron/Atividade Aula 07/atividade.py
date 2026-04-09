def inserir_cliente(fila, nome):
    fila.append(nome)

def remover_primeiro(fila):
    if len(fila) == 0:
        return None

    primeiro = fila[0]

    for i in range(len(fila) - 1):
        fila[i] = fila[i + 1]

    fila.pop()
    return primeiro

def buscar_cliente(fila, nome):
    for i in range(len(fila)):
        if fila[i] == nome:
            return i
    return -1

def exibir_fila(fila):
    print("Fila atual:", fila)

fila = []

inserir_cliente(fila, "Ana")
inserir_cliente(fila, "Carlos")
inserir_cliente(fila, "Marina")

exibir_fila(fila)

cliente = remover_primeiro(fila)
print("Cliente atendido:", cliente)

posicao = buscar_cliente(fila, "Carlos")
print("Posição encontrada:", posicao)

exibir_fila(fila)