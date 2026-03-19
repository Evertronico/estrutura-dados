def analisar_vendas(vendas):
    if not vendas:
        print("Nenhum dado de venda para analisar.")
        return

    tamanho = len(vendas)

    media = sum(vendas) / tamanho

    vendas_ordenadas = vendas[:]
    for i in range(tamanho):
        for j in range(0, tamanho - i - 1):
            if vendas_ordenadas[j] > vendas_ordenadas[j + 1]:
                vendas_ordenadas[j], vendas_ordenadas[j + 1] = vendas_ordenadas[j + 1], vendas_ordenadas[j]

    meio = tamanho // 2
    if tamanho % 2 == 0:
        mediana = (vendas_ordenadas[meio - 1] + vendas_ordenadas[meio]) / 2.0
    else: 
        mediana = vendas_ordenadas[meio]

    acima_da_media = sum(1 for v in vendas if v > media)

    print("Relatório de Vendas")
    print(f"Vendas registradas: {vendas}")
    print(f"Vendas (Ordenadas): {vendas_ordenadas}")
    print(f"Média de vendas:    R$ {media:.2f}")
    print(f"Mediana de vendas:  R$ {mediana:.2f}")
    print(f"Dias acima da média: {acima_da_media}")

vendas_diarias = [150.0, 200.5, 90.0, 300.0, 180.0, 400.0, 120.0]
analisar_vendas(vendas_diarias)