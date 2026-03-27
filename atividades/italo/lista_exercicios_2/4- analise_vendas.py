def calcular_media(lista):
    soma = 0
    for valor in lista:
        soma += valor
    return soma / len(lista)

def ordenar(lista):
    nova_lista = lista.copy()
    n = len(nova_lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if nova_lista[j] > nova_lista[j + 1]:
                # troca
                temp = nova_lista[j]
                nova_lista[j] = nova_lista[j + 1]
                nova_lista[j + 1] = temp

    return nova_lista

def calcular_mediana(lista):
    ordenada = ordenar(lista)
    n = len(ordenada)

    if n % 2 == 1:
        return ordenada[n // 2]
    else:
        meio1 = ordenada[(n // 2) - 1]
        meio2 = ordenada[n // 2]
        return (meio1 + meio2) / 2

def contar_acima_media(lista, media):
    contador = 0
    for valor in lista:
        if valor > media:
            contador += 1
    return contador

def analisar_vendas(vendas):
    media = calcular_media(vendas)
    mediana = calcular_mediana(vendas)
    acima = contar_acima_media(vendas, media)

    print("=== Análise de Vendas ===")
    print("Vendas:", vendas)
    print("Média:", f"{media:.2f}")
    print("Mediana:", mediana)
    print("Quantidade acima da média:", acima)

vendas = [100, 200, 150, 300, 250, 400, 50]

analisar_vendas(vendas)