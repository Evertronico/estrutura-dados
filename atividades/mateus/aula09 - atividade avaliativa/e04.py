# Exercício 4 – Análise de Desempenho de Vendas
# Implemente um sistema que analise dados de vendas diárias de uma empresa a partir de uma lista de valores numéricos.
# Requisitos:
#  * Calcular média das vendas
#  * Calcular mediana (ordenar manualmente ou por lógica implementada)
#  * Contar quantos valores estão acima da média
#  * Não utilizar bibliotecas externas
#  * Exibir resultados de forma organizada

def inserir(lista, valor):
    lista.append(valor);
    organiza(lista)

def organiza(lista):
    for i in range(len(lista) -1, 0, -1):
        for j in range(i):
            if lista[j] > lista[j+1]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp

def calcular_soma(lista):
    total = 0
    for nota in lista:
        total+=nota
    return total

def media(lista):
    somaTotal = calcular_soma(lista)
    return somaTotal/ len(lista)

def contAcimaMedia(lista, media):
    acimaMedia = 0
    for valor in lista:
        if valor > media:
            acimaMedia+=1
    return acimaMedia

def mediana(lista):
    organiza(lista)
    tamanho = len(lista)
    meio = int((tamanho - 1) / 2)
    if (tamanho % 2 == 0):
        print('As medianas são :')
        print(lista[meio])
        print(lista[meio + 1])
    else:
        print(f'A mediana é {lista[meio]}')

vendas = [12,4,7,23,38]

print(f'A média e {media(vendas)}')
print(f'A quantidade de valor acima da media é {contAcimaMedia(vendas,media(vendas))}')
print(f'O valor organizado é ')
organiza(vendas)
for index,venda in enumerate(vendas):
            print(f'{index} - {venda}') 

mediana(vendas)