lista = []

soma = 0
maior = None
menor = None

for i in range(5):
    n = int(input('Digite um número: '))

    lista.append(None)

    lista[i] = n

    soma += lista[i]

    if i == 0:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n

media = soma / len(lista)

print(lista)
print(f'A soma dos elementos é {soma}')
print(f'A média dos elementos é {media}')
print(f'O maior elemento na lista é {maior}')
print(f'O menor elemento na lista é {menor}')