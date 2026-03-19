vendas = [10, 20, 30, 32, 111, 24278, 122]

def media(lista):
    some = 0
    for v in lista:
        soma += v
    return soma / len(lista)

def ordenar(lista):
    l = lista[:]
    for i in range(len(l)):
        for j in range(len(l)-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], i[j]
    return l

def mediana(lista):
    l = ordenar(lista)
    meio = len(l)/2
    return l[meio]

def acimamedia(lista):
    m = media(lista)
    cont = 0
    for v in lista:
        if v > m:
            cont += 1
    return cont

