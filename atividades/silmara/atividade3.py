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

def remover(lista, valor):
    n = len(lista)
    indice_alvo = -1

    for i in range(n):
        if lista[i] == valor:
            indice_alvo = i
            break
    
    if indice_alvo != -1:
        for j in range(indice_alvo, n - 1):
            lista[j] = lista[j + 1]
        del lista[-1]
        print(f"Elemento {valor} removido.")
    else:
        print(f"Valor {valor} não encontrado para remoção.")
    
    return lista

dados = [20, 45, 88, 751, 0.0, 0.1]
print(f"Lista original: {dados}")
remover(dados, 45)
print(f"Lista atualizada: {dados}")