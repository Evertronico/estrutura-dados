def analisar_vendas(vendas):
    if len(vendas) == 0:
        return

    soma = 0
    for valor in vendas:
        soma += valor
    media = soma / len(vendas)

    vendas_ord = vendas[:] 
    n = len(vendas_ord)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if vendas_ord[j] > vendas_ord[j + 1]:
                vendas_ord[j], vendas_ord[j + 1] = vendas_ord[j + 1], vendas_ord[j]

    meio = n // 2
    if n % 2 == 0:
        mediana = (vendas_ord[meio - 1] + vendas_ord[meio]) / 2
    else:
        mediana = vendas_ord[meio]

    acima_da_media = 0
    for valor in vendas:
        if valor > media:
            acima_da_media += 1

    print(f"Média: {media:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Valores acima da média: {acima_da_media}")

dados = [150.0, 200.0, 100.0, 300.0, 250.0]
analisar_vendas(dados)