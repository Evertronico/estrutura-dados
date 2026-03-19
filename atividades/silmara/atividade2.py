# Atividade 2 — Busca Sequencial
# Implemente uma função chamada:
# busca_sequencial(lista, valor)
# A função deve percorrer a lista e retornar:
# o índice do elemento encontrado
# -1 caso o valor não esteja presente.
# Não utilize:
# index()
# in

def busca_sequencial(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1

numeros = [13, 67, 973, 0.5, 20, 70, 99]
alvo = 973
resultado = busca_sequencial(numeros, alvo)

if resultado != -1:
    print(f"Valor {alvo} encontrado no índice: {resultado}")
else:
    print(f"Valor {alvo} não encontrado.")