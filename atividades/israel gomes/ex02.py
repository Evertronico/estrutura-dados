import random

def busca_sequencial(lista, valor):
    result = -1

    for i, value in enumerate(lista):
        if value == valor:
            result = i
            break
    
    return result

lista_dados = [1.0, 2.5, 9.9, 4.7, 7.8, 9.2, 8.8, 6.5, 8.0, 5.0]

n_procurados = [random.randint(0, 100) / 10 for i in range(10)]

for n in n_procurados:
    encontrado = busca_sequencial(lista_dados, n)
    if encontrado == -1:
        print(f'Número {n} não foi encontrado na lista')
    else:
        print(f'Número {n} foi encontrado pela primeira vez na lista na posição {encontrado}')