# Atividade 3 — Remoção Manual de Elemento
# Implemente uma função que remova um elemento de uma lista sem utilizar métodos prontos.
# Função esperada:
# remover(lista, valor)
# O algoritmo deve:
# localizar o elemento
# deslocar os elementos à direita
# atualizar a lista resultante
# Não utilizar:
# remove()
# pop()

def removerValor(lista, valor):
    if valor < 0 or valor >= len(lista):
        return IndexError("A posicao na lista e invalida")
    
    removido = lista[valor]

    for i in range(valor, len(lista) - 1):
        lista[i] = lista[i + 1]
    
    del lista[i]

    return removido

dados = [10, 20, 30, 40, 50]
valorRemovido = removerValor(dados, 1)

print("O valor ", valorRemovido, " foi removido")
print("Os valores restantes sao: ", dados)