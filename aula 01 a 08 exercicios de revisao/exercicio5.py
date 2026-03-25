def adicionar(fila, nome):
    fila.append(nome)


def atender(fila):
    if len(fila) == 0:
        print("Fila vazia.")
        return

    atendido = fila[0]

    # deslocamento manual
    for i in range(0, len(fila) - 1):
        fila[i] = fila[i + 1]

    fila.pop()

    print("Atendido:", atendido)


def exibir(fila):
    if len(fila) == 0:
        print("Fila vazia.")
        return

    for pessoa in fila:
        print(pessoa)


# Teste
fila = []

adicionar(fila, "Ana")
adicionar(fila, "Carlos")
adicionar(fila, "Maria")

atender(fila)

exibir(fila)