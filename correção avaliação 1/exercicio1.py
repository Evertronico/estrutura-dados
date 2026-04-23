numeros = []
for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

soma = 0
maior = numeros[0]
menor = numeros[0]

for n in numeros:
    soma += n
    if n > maior: maior = n
    if n < menor: menor = n

media = soma / 5
print(f"Soma: {soma}, Média: {media}, Maior: {maior}, Menor: {menor}")