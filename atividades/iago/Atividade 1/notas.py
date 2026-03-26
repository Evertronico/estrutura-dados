# Atividade 1 - Estatísticas de Notas
notas = [8.5, 7.0, 9.5, 6.0, 10.0, 4.5, 7.5, 8.0, 5.5, 9.0]

# Média, Maior e Menor
soma = 0
maior = notas[0]
menor = notas[0]

for n in notas:
    soma += n
    if n > maior: maior = n
    if n < menor: menor = n

media = soma / len(notas)

# Ordenação Manual (Bubble Sort)
n_elementos = len(notas)
for i in range(n_elementos):
    for j in range(0, n_elementos - i - 1):
        if notas[j] > notas[j + 1]:
            # Troca de posição manual
            temp = notas[j]
            notas[j] = notas[j + 1]
            notas[j + 1] = temp

print(f"Média: {media:.2f}")
print(f"Maior: {maior} | Menor: {menor}")
print(f"Notas Ordenadas: {notas}")