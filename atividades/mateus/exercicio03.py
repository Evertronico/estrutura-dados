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



def procura(lista,valor):
    for i in range(len(lista)):
       if lista[i] == valor:
           return i
    return -1

def remover(lista, valor):
    posicao = procura(lista,valor)
    if(posicao == -1):
        return
    for i in range(posicao, len(lista)-1):
        lista[i] = lista[i+1]
    lista[-1] = None
    

nums = [2,3,4,5]
remover(nums,3)
print(nums)
