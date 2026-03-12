# Atividade 4 — Inserção Ordenada em Lista
# Implemente uma função que insira um valor em uma lista mantendo a ordem crescente dos elementos.
# Função esperada:
# inserir_ordenado(lista, valor)
# A função deve:
# encontrar a posição correta do novo elemento
# deslocar os elementos necessários para a direita
# inserir o valor na posição correta
# Não utilizar:
# sort()
# insert()

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

lista = [3,2,1]
inserir(lista,0)

print(lista)