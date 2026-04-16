numeros = []

def adicionar(lista,valor):
    lista.append(0)
    for i in range(len(lista)-1, 0, -1):  
        lista[i] = lista[i-1]
    lista[0] = valor

def procura(lista,valor):
    for i in range(len(lista)-1):
        if lista[i] == valor:
            return i
    return -1

def remover(lista,valor):
    posicao = procura(lista,valor)
    
    for i in range(posicao, len(lista)-1):  
        lista[i] = lista[i+1]
    lista.pop()

def listar(lista):
    for i in range(len(lista)):
        print(lista[i])

def preencherLista(lista,qtd):
    for i in range(qtd):
        num = int(input("Informe um número: "))
        adicionar(lista,num)

while True:
    print("1 - inserir")
    print("2 - apagar")
    print("3 - listar")
    print("4 - busca")
    print("0 - parar")
    
    opcao = int(input("Informe a opção :"))
     
    if opcao == 0:
        print("Programa encerrado")
        break
    else:
        if opcao == 1:
            qtd = int(input("Informe a quantidade para inserir :"))
            preencherLista(numeros,qtd)

        if opcao == 2:
            num = int(input("Informe o numero para deletar :"))
            remover(numeros,num)
        
        if opcao == 3:
            listar(numeros)
            
        if opcao == 4:
            num = int(input("Informe o numero para buscar :"))
            indice = procura(numeros,num)
            if (indice < 0):
                print("Numero não existe na lista")
            else:
                print(numeros[indice])