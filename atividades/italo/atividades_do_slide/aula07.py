fila = []

def inserir(nome):
    fila.append(nome)

def remover():
    if len(fila) == 0:
        return None
    primeiro = fila[0]
    nova = []
    i = 1
    while i < len(fila):
        nova.append(fila[i])
        i += 1
    fila.clear()
    for item in nova:
        fila.append(item)
    return primeiro

def buscar(nome):
    i = 0
    while i < len(fila):
        if fila[i] == nome:
            return i
        i += 1
    return -1

def mostrar():
    i = 0
    while i < len(fila):
        print(fila[i])
        i += 1

while True:
    op = input()
    
    if op == "1":
        inserir(input())
    elif op == "2":
        print(remover())
    elif op == "3":
        print(buscar(input()))
    elif op == "4":
        mostrar()
    elif op == "5":
        break