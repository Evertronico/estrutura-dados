numeros = []
soma = 0
    
def adicionar(lista,valor):
    lista.append(0)
    for i in range(len(lista)-1, 0, -1):  
        lista[i] = lista[i-1]
    lista[0] = valor

def maior(lista):
    maiorNum = lista[0]
    for i in range(len(lista)-1):
        if lista[i] > maiorNum:
            maiorNum = lista[i]
    return maiorNum

def menor(lista):
    menorNum = lista[0]
    for i in range(len(lista)-1):
        if lista[i] < menorNum:
            menorNum = lista[i]
    return menorNum

for i in range(5):
    num = int(input("Informe um número: "))
    soma += num
    adicionar(numeros,num)


maiorNumero = maior(numeros)
menorNumero = menor(numeros)

print(f"A soma é {soma}")
print(f"A média é {soma/len(numeros)}")
print(f"O menor numero é {menorNumero}")
print(f"O maior numero é {maiorNumero}")


