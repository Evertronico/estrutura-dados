"""2. Implemente um TAD de Lista de Números, utilizando funções em Python.

O TAD deve oferecer as seguintes operações:

    Inserir elemento
    Remover elemento
    Buscar elemento (retornar se existe ou não)
    Exibir todos os elementos"""

def inserir(lista, valor):
    lista.append(None)

    lista[len(lista) - 1] = valor

    return lista

def buscar(lista, valor):
    result = -1

    for i, value in enumerate(lista):
        if value == valor:
            result = i
            break
    
    return result

def remover(lista, valor):
    encontrado = buscar(lista, valor)

    if encontrado == -1:
        return lista
    
    for i in range(encontrado, len(lista) -1):
        lista[i] = lista[i + 1]
    
    del lista[i + 1]

    return lista

def exibir_lista(lista):
    print(lista)

lista = []

while True:
    msg = '''Escolha uma opção:

1. Inserir elemento
2. Remover elemento
3. Buscar elemento (retornar se existe ou não)
4. Exibir todos os elementos
0. Sair'''

    print(msg)

    opcao_escolhida = int(input('>> '))

    if (opcao_escolhida == 1):
        n = int(input('Digite um número: '))

        inserir(lista, n)
    elif (opcao_escolhida == 2):
        n = int(input('Digite um número para exluir da lista: '))

        remover(lista, n)
    elif (opcao_escolhida == 3):
        n = int(input('Digite um número para buscar na lista: '))

        encontrado = buscar(lista, n)

        if encontrado == -1:
            print(f'O valor {n} não foi encontrado na lista')
        else:
            print(f'O valor {n} foi encontrado na posição {encontrado} da lista')
    elif (opcao_escolhida == 4):
        exibir_lista(lista)
    
    elif opcao_escolhida == 0:
        break

    else:
        print('Opção inválida')