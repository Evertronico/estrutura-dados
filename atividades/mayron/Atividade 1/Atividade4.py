dados = [10, 20, 30, 40, 50]

def inserir_ordenado(lista, valor):
    posicao = len(lista) 
    
    for i in range(len(lista)):
        if lista[i] > valor:
            posicao = i
            break
            
    lista.append(None)
    
    for i in range(len(lista) - 1, posicao, -1):
        lista[i] = lista[i - 1]
        
    lista[posicao] = valor

inserir_ordenado(dados, 25)
print(dados)
