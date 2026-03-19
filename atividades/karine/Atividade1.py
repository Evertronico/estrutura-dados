notas = [7.5, 6.9, 3, 8.7, 5.2, 9, 7.7, 1, 1.2, 6.3]

# 2. Cálculos de Média, Maior e Menor
media = sum(notas) / len(notas)
NotaMaior = max(notas)
NotaMenor = min(notas)

notasCresc = list(notas) 
n = len(notasCresc)

for i in range(n):
    for j in range(0, n - i - 1):

        if notasCresc[j] > notasCresc[j + 1]:
            notasCresc[j], notasCresc[j + 1] = notasCresc[j + 1], notasCresc[j]

print("-" * 30)
print(f"A média da turma é de: {media:.2f}")
print(f"A maior nota é: {NotaMaior}")
print(f"A menor nota é: {NotaMenor}")
print(f"Notas em ordem crescente: {notasCresc}")