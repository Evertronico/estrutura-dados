# Atividade 2 - Ex 3: Inserção Ordenada
def inserir_ordenado(lista, valor):
    posicao = len(lista)
    for i in range(len(lista)):
        if lista[i] > valor:
            posicao = i
            break
    
    lista[:] = lista + [0]
    for i in range(len(lista) - 1, posicao, -1):
        lista[i] = lista[i - 1]
    
    lista[posicao] = valor

# Teste
precos = [10.5, 20.0, 35.5]
inserir_ordenado(precos, 25.0)
print(f"Preços ordenados: {precos}")