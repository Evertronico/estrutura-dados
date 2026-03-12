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

def inserirValor(lista, valor, posicao):
    if posicao < 0 or posicao > len(lista):
       raise IndexError("Posicao invalida")
    
    lista.append(None)

    for i in range(len(lista) -1, posicao, -1):
        lista[i] = lista[i - 1]

    lista[posicao] = valor

dados = [50, 60, 95, 28]
dadoInserido = inserirValor(dados, 99, 0)

print("Lista atual: ", dados)