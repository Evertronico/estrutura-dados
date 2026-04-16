numeros = [1,3,4]

def adicionar(lista,valor,posicao):
    lista.append(0)
    for i in range(len(lista)-1, posicao, -1):  
        lista[i] = lista[i-1]
    lista[posicao] = valor

def procura(lista,valor):
    for i in range(len(lista)-1):
        if lista[i] == valor:
            return i
    return -1

def remover(lista,posicao):
    for i in range(posicao, len(lista)-1):  
        lista[i] = lista[i+1]
    lista.pop()
    
def listar(lista):
    for i in range(len(lista)):
        print(f"{lista[i]}")
        

adicionar(numeros,10,1)
remover(numeros,1)
posicao = procura(numeros, 3)
print(f"O numero está na posicao : {posicao}")
listar(numeros)

