def ordenar(lista):
    # bubble sort
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


def media(lista):
    soma = 0
    for valor in lista:
        soma += valor
    return soma / len(lista)


def mediana(lista):
    copia = lista[:]
    ordenar(copia)

    n = len(copia)

    if n % 2 == 0:
        return (copia[n//2 - 1] + copia[n//2]) / 2
    else:
        return copia[n//2]


def acima_media(lista):
    m = media(lista)
    contador = 0

    for valor in lista:
        if valor > m:
            contador += 1

    return contador


# Teste
vendas = [100, 200, 150, 300, 250]

print("Média:", media(vendas))
print("Mediana:", mediana(vendas))
print("Acima da média:", acima_media(vendas))