# Lista com valores de vendas (exemplo)
vendas = [120, 80, 200, 150, 90, 300, 50]

# -------------------------
# Função para calcular média
# -------------------------
def calcular_media(lista):
    soma = 0
    
    # Soma todos os valores manualmente
    for i in range(len(lista)):
        soma += lista[i]
    
    media = soma / len(lista)
    return media


# -------------------------
# Função para ordenar (sem usar sort)
# Aqui usei um método simples (Bubble Sort)
# -------------------------
def ordenar_lista(lista):
    lista_ordenada = lista.copy()  # não altera a original
    
    for i in range(len(lista_ordenada)):
        for j in range(0, len(lista_ordenada) - 1):
            if lista_ordenada[j] > lista_ordenada[j + 1]:
                # troca os valores de lugar
                temp = lista_ordenada[j]
                lista_ordenada[j] = lista_ordenada[j + 1]
                lista_ordenada[j + 1] = temp
    
    return lista_ordenada


# -------------------------
# Função para calcular mediana
# -------------------------
def calcular_mediana(lista):
    ordenada = ordenar_lista(lista)
    n = len(ordenada)
    
    # Se quantidade for ímpar → pega o do meio
    if n % 2 != 0:
        meio = n // 2
        return ordenada[meio]
    else:
        # Se for par → média dos dois do meio
        meio1 = (n // 2) - 1
        meio2 = n // 2
        return (ordenada[meio1] + ordenada[meio2]) / 2


# -------------------------
# Função para contar valores acima da média
# -------------------------
def contar_acima_media(lista, media):
    contador = 0
    
    for i in range(len(lista)):
        if lista[i] > media:
            contador += 1
    
    return contador


# -------------------------
# Função principal para análise
# -------------------------
def analisar_vendas(lista):
    print("\n=== ANÁLISE DE VENDAS ===")
    
    media = calcular_media(lista)
    mediana = calcular_mediana(lista)
    acima = contar_acima_media(lista, media)
    
    print(f"Vendas: {lista}")
    print(f"Média das vendas: {media:.2f}")
    print(f"Mediana das vendas: {mediana}")
    print(f"Quantidade acima da média: {acima}")


# -------------------------
# Executando
# -------------------------
analisar_vendas(vendas)