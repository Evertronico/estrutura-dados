numeros = []

for i in range(5):
    while True:
        try:
            n = int(input(f"Digite o {i+1}º número: "))
            numeros.append(n)
            break
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")

soma = 0
for n in numeros:
    soma += n

media = soma / 5

maior = numeros[0]
menor = numeros[0]

for n in numeros:
    if n > maior:
        maior = n
    if n < menor:
        menor = n

print("Soma:", soma)
print("Média:", media)
print("Maior:", maior)
print("Menor:", menor)