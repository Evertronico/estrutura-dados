# Exercício 4 – Análise de Desempenho de Vendas
# Implemente um sistema que analise dados de vendas diárias de uma empresa a partir de uma lista de valores numéricos.
# Requisitos:
#  * Calcular média das vendas
#  * Calcular mediana (ordenar manualmente ou por lógica implementada)
#  * Contar quantos valores estão acima da média
#  * Não utilizar bibliotecas externas
#  * Exibir resultados de forma organizada

vendas = [100, 250, 150, 400, 300]

def analisar_vendas(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    
    media = sum(lista) / n
    
    meio = n // 2
    mediana = lista[meio] if n % 2 != 0 else (lista[meio-1] + lista[meio]) / 2
    
    acima = 0
    for v in lista:
        if v > media: acima += 1
            
    print(f"Média: {media}")
    print(f"Mediana: {mediana}")
    print(f"Vendas Acima da Média: {acima}")

analisar_vendas(vendas)