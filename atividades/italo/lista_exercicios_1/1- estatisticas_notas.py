notas = [7.5, 8.0, 6.5, 9.0, 5.5, 10.0, 7.0, 8.5, 6.0, 9.5]

soma = 0
for nota in notas:
    soma += nota
media = soma / len(notas)

maior = notas[0]
menor = notas[0]

for nota in notas:
    if nota > maior:
        maior = nota
    if nota < menor:
        menor = nota

notas_ordenadas = notas.copy()

for i in range(len(notas_ordenadas)):
    for j in range(0, len(notas_ordenadas) - i - 1):
        if notas_ordenadas[j] > notas_ordenadas[j + 1]:

            temp = notas_ordenadas[j]
            notas_ordenadas[j] = notas_ordenadas[j + 1]
            notas_ordenadas[j + 1] = temp

print("Notas:", notas)
print("Média da turma:", media)
print("Maior nota:", maior)
print("Menor nota:", menor)
print("Notas em ordem crescente:", notas_ordenadas)