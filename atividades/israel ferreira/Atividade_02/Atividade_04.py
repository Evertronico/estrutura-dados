'''
    Exercício 4 – Análise de Desempenho de Vendas
    Implemente um sistema que analise dados de vendas diárias de uma empresa a partir de uma lista de valores numéricos.
    Requisitos:
    * Calcular média das vendas
    * Calcular mediana (ordenar manualmente ou por lógica implementada)
    * Contar quantos valores estão acima da média
    * Não utilizar bibliotecas externas
    * Exibir resultados de forma organizada

'''
vendas = []

def adicionar_venda(valor):
    vendas.append(valor)

def calcular_media():
    if not vendas: return 0
    soma = 0
    for v in vendas:
        soma += v
    return soma / len(vendas)

def calcular_mediana():
    if not vendas: return 0
    
    # Clonar e ordenar manualmente (Bubble Sort)
    lista_ordenada = vendas[:]
    n = len(lista_ordenada)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_ordenada[j] > lista_ordenada[j + 1]:
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]
    
    meio = n // 2
    if n % 2 == 0:
        return (lista_ordenada[meio - 1] + lista_ordenada[meio]) / 2
    else:
        return lista_ordenada[meio]

def contar_acima_media(media):
    contagem = 0
    for v in vendas:
        if v > media:
            contagem += 1
    return contagem

while True:
    print('=' * 50)
    print('||    <<<<<<<<<<ANALISE DE VENDAS>>>>>>>>>>    ||')
    print('||    1) -REGISTRAR VENDA..................:    ||')
    print('||    2) -EXIBIR RELATÓRIO.................:    ||')
    print('||    3) -SAIR.............................:    ||')
    print('=' * 50)

    opcao = input("- ")
    if opcao == "1":
        valor = float(input("Valor da venda: "))
        adicionar_venda(valor)
        print("Venda registrada!")
    elif opcao == "2":
        if not vendas:
            print("Nenhuma venda registrada.")
        else:
            media = calcular_media()
            mediana = calcular_mediana()
            acima = contar_acima_media(media)
            print("-" * 50)
            print(f"Total de vendas: {len(vendas)}")
            print(f"Média: R$ {media:.2f}")
            print(f"Mediana: R$ {mediana:.2f}")
            print(f"Vendas acima da média: {acima}")
    elif opcao == "3":
        break