'''3. Implemente manualmente uma estrutura de lista sequencial (simulando vetor),
    sem utilizar métodos prontos de listas Python.

A estrutura deve permitir:

    Inserção em uma posição específica
    Remoção de um elemento (com deslocamento manual dos elementos)
    Busca sequencial
    Exibição dos elementos'''

from time import sleep

def inserir_posicao(lista, valor, posicao):
    if posicao > len(lista):
        posicao = len(lista)

    lista.append(None)
    
    for y in range(len(lista) - 1, posicao, -1):
        lista[y] = lista[y -1]

    lista[posicao] = valor

def busca_sequencial(lista, valor):
    result = -1

    for i, value in enumerate(lista):
        if value == valor:
            result = i
            break
    
    return result

def exibir_lista(lista):
    print(lista)

def intervalo():
    print('')

    sleep(2)

lista = [4.0, 3.7, 9.8, 4.4, 5.1]

print('Lista:')
exibir_lista(lista)

intervalo()

valor = 6.7
posicao = 2

print(f'Inserindo \'{valor}\' na posição {posicao}')

intervalo()

inserir_posicao(lista, valor, posicao)

exibir_lista(lista)

intervalo()

n1_procurado = 4.4

print(f'Procurando \'{n1_procurado}\' na lista')

intervalo()

n1_encontrado = busca_sequencial(lista, n1_procurado)

print(f'Valor {n1_procurado} encontrado na posição {n1_encontrado} da lista (-1 significa que não foi encontrado)')

intervalo()

n2_procurado = 9.0

print(f'Procurando \'{n2_procurado}\' na lista')

intervalo()

n2_encontrado = busca_sequencial(lista, n2_procurado)

print(f'Valor {n2_procurado} encontrado na posição {n2_encontrado} da lista (-1 significa que não foi encontrado)')

intervalo()

print('Exibindo lista:')

exibir_lista(lista)
