# Lista para armazenar as notas
notas = []

# Entrada de dados
for i in range(10):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

# Cálculo da média
soma = 0
for n in notas:
    soma += n
media = soma / len(notas)

# Maior e menor nota
maior = notas[0]
menor = notas[0]

for n in notas:
    if n > maior:
        maior = n
    if n < menor:
        menor = n

ordenadas = notas.copy()

for i in range(len(ordenadas)):
    for x in range(len(ordenadas) - 1):
        if ordenadas[x] > ordenadas[x + 1]:
            temp = ordenadas[x]
            ordenadas[x] = ordenadas[x + 1]
            ordenadas[x + 1] = temp

# Exibição dos resultados
print("\nResultados:")
print(f"Média da turma: {media:.2f}")
print(f"Maior nota: {maior}")
print(f"Menor nota: {menor}")
print(f"Notas em ordem crescente: {ordenadas}")