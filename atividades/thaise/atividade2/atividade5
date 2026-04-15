fila = []

def adicionar(nome):
    fila.append(nome)

def atender():
    if len(fila) == 0:
        print("Fila vazia")
        return

    atendido = fila[0]

    # deslocar
    for i in range(len(fila) - 1):
        fila[i] = fila[i + 1]

    # remover último
    nova = []
    for i in range(len(fila) - 1):
        nova.append(fila[i])

    print("Atendido:", atendido)
    return nova

def exibir():
    print("Fila:", fila)


# uso
fila.append("Ana")
fila.append("João")

exibir()
fila = atender()
exibir()