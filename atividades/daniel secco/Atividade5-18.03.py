fila = []

def entrar(nome):
    fila.append(nome)

def atender():
    if len(fila) == 0:
        print("A fila está vazia")
        return
    
    atendido = fila[0]
    nova = []

    for i in range(1, len(fila)):
        nova.append(fila[i])


        return atendido, nova
    
def mostrar():
    for p in fila:
        print(p)