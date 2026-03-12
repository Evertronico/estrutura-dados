numeros = [10, 20, 30, 40, 50, 60]

maior = numeros[0]
menor = numeros[0]

indiceMaior = 0
indiceMenor = 0

for i in range(len(numeros)):
    if numeros[i] > maior:
        maior = numeros[i]
        indiceMaior = i

    if numeros[i] < menor:
        menor = numeros[i]
        indiceMenor = i

numeros.pop(indiceMaior)

if indiceMenor > indiceMaior:
    indiceMenor -= 1

numeros.pop(indiceMenor)

soma = 0

for n in numeros:
    soma = soma + n

media = soma / len(numeros)

print("Maior valor:", maior)
print("Menor valor:", menor)
print("Numeros restantes:", numeros)
print("Media dos valores: ", media)