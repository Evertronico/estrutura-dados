def ordenar(lista):
    nova_lista = []
    for item in lista:
        nova_lista.append(item)

    for i in range(len(nova_lista)):
        for j in range(len(nova_lista) - 1):
            if nova_lista[j] > nova_lista[j + 1]:
                temp = nova_lista[j]
                nova_lista[j] = nova_lista[j + 1]
                nova_lista[j + 1] = temp

    return nova_lista

def calcular_media(lista):
    soma = 0
    for valor in lista:
        soma += valor
    return soma / len(lista)

def calcular_mediana(lista):
    ordenada = ordenar(lista)
    n = len(ordenada)

    if n % 2 == 0:
        meio1 = ordenada[n // 2 - 1]
        meio2 = ordenada[n // 2]
        return (meio1 + meio2) / 2
    else:
        return ordenada[n // 2]

def acima_da_media(lista, media):
    contador = 0
    for valor in lista:
        if valor > media:
            contador += 1
    return contador

vendas = []
quantidade = int(input("Quantos dias de vendas deseja informar? "))

for i in range(quantidade):
    valor = float(input(f"Digite o valor do dia {i+1}: "))
    vendas.append(valor)

media = calcular_media(vendas)
mediana = calcular_mediana(vendas)
acima = acima_da_media(vendas, media)

print("\nANÁLISE DE VENDAS")
print(f"Média das vendas: {media:.2f}")
print(f"Mediana das vendas: {mediana:.2f}")
print(f"Quantidade de dias acima da média: {acima}")