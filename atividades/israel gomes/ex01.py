notas = [1.0, 2.5, 9.9, 4.7, 7.8, 9.2, 8.8, 6.5, 8.0, 5.0]

print(len(notas))

soma = 0
maior = None
menor = None

for nota in notas:
    soma += nota

    if maior == None:
        maior = nota
        menor = nota
    else:
        if nota > maior:
            maior = nota
        elif nota < menor:
            menor = nota

media = soma / len(notas)

for x in range(len(notas) - 1, 0, -1):
    for y in range(x):
        if notas[y] > notas[y + 1]:
            notas[y], notas[y + 1] = notas[y + 1], notas[y]

print(f'Média das notas: {media:.2f}')
print(f'Maior nota: {maior}')
print(f'Menor nota: {menor}')
print(f'Lista ordenada: {notas}')