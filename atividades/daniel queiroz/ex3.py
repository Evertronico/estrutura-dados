#Exercício 3 – Inserção Ordenada de Dados
#Implemente uma função que insira valores em uma lista mantendo a ordenação crescente, simulando um sistema que organiza automaticamente dados numéricos.
#Requisitos:
# * Lista deve permanecer ordenada após cada inserção
# * Encontrar posição correta manualmente
# * Deslocar elementos sem usar insert()
# * Não utilizar sort()
# * Implementar função reutilizável


numeros = []

def inserirOrdenado(valor):
    if not isinstance(valor, (int, float)):
        print("Valor deve ser um número")
        return
    
    if len(numeros) == 0:
        numeros.append(valor)
        print(f"Valor {valor} inserido na posição 0")
        return
    
    posicao = 0
    i = 0
    while i < len(numeros):
        if valor <= numeros[i]:
            posicao = i
            break
        posicao = i + 1
        i += 1
    
    numeros.append(None) 
    
    i = len(numeros) - 2
    while i >= posicao:
        numeros[i + 1] = numeros[i]
        i -= 1
    
    numeros[posicao] = valor
    print(f"Valor {valor} inserido na posição {posicao}")

def exibirLista():
    print("\n=== LISTA ORDENADA ===")
    if len(numeros) == 0:
        print("Lista vazia\n")
        return
    
    print("Posição | Valor")
    i = 0
    while i < len(numeros):
        print(f"   {i}    |  {numeros[i]}")
        i += 1
    print()

def buscarValor(valor):
    i = 0
    while i < len(numeros):
        if numeros[i] == valor:
            print(f"Valor {valor} encontrado na posição {i}")
            return
        i += 1
    print(f"Valor {valor} não encontrado")


print("| INSERÇÃO ORDENADA |\n")

inserirOrdenado(50)
exibirLista()

inserirOrdenado(30)
exibirLista()

inserirOrdenado(70)
exibirLista()

inserirOrdenado(10)
exibirLista()

inserirOrdenado(100)
exibirLista()

inserirOrdenado(25)
exibirLista()

inserirOrdenado(60)
exibirLista()


buscarValor(30)
buscarValor(15)

exibirLista()