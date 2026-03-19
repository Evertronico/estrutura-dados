# Exercício 3 – Inserção Ordenada de Dados
# Implemente uma função que insira valores em uma lista mantendo a ordenação crescente, simulando um sistema que organiza automaticamente dados numéricos.
# Requisitos:
#  * Lista deve permanecer ordenada após cada inserção
#  * Encontrar posição correta manualmente
#  * Deslocar elementos sem usar insert()
#  * Não utilizar sort()
#  * Implementar função reutilizável

def inserir(lista, valor):
    lista.append(valor);
    organiza(lista)

def organiza(lista):
    for i in range(len(lista) -1, 0, -1):
        for j in range(i):
            if lista[j] > lista[j+1]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp



nums = []
cont = 0
while (cont <= 5):
    num = int(input('Informe um numero: '))
    inserir(nums,num)
    print(nums)
    cont = cont + 1