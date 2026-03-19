'''
Atividade 2 — Busca Sequencial
Implemente uma função chamada:
busca_sequencial(lista, valor)
A função deve percorrer a lista e retornar:
o índice do elemento encontrado
-1 caso o valor não esteja presente.
Não utilize:
index()
in
'''

def busca_sequencial(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i  
    return -1 

numeros = [15, 20, 25, 40, 45]

procurado = int(input("Digite o valor a buscar: "))

resultado = busca_sequencial(numeros, procurado)

if resultado != -1:
    print(f"Valor encontrado no índice {resultado}")
else:
    print("Valor não encontrado")