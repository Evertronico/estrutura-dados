'''
Atividade 4 — Inserção Ordenada em Lista
Implemente uma função que insira um valor em uma lista mantendo a ordem crescente dos elementos.
Função esperada:
inserir_ordenado(lista, valor)
A função deve:
encontrar a posição correta do novo elemento
deslocar os elementos necessários para a direita
inserir o valor na posição correta
Não utilizar:
sort()
insert()
'''
def inserir_ordenado(lista, valor):
    nova_lista = []
    for item in lista:
        nova_lista.append(item)
    nova_lista.append(0)  

    pos = 0
    while pos < len(lista) and lista[pos] < valor:
        pos += 1
    for i in range(len(nova_lista) - 1, pos, -1):
        nova_lista[i] = nova_lista[i - 1]

    nova_lista[pos] = valor

    return nova_lista

numeros = [10, 20, 30, 40, 50]

valor = int(input("Digite o valor a inserir: "))

numeros = inserir_ordenado(numeros, valor)

print("Lista atualizada:", numeros)