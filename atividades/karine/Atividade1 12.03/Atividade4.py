NotasOrd = [1, 2, 2.2, 5.5, 6, 7.3, 8.2, 8.9, 9.5]

def inserir_ordenado(lista, valor):
    lista.append(0) 
    
    posicao = len(lista) - 1
    
    while posicao > 0 and lista[posicao - 1] > valor:
        lista[posicao] = lista[posicao - 1] 
        posicao -= 1 
        
    lista[posicao] = valor
    
    return lista

NovaNota = 7.1

resultado = inserir_ordenado(NotasOrd, NovaNota)
print(f"Lista atualizada: {resultado}")