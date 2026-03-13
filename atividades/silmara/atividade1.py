# Atividade 1 — Estatísticas de Notas
# Crie um programa que armazene 10 notas de alunos em uma lista.
# O programa deve calcular e exibir:
# média da turma
# maior nota
# menor nota
# lista de notas ordenadas em ordem crescente
# Não utilize a função sort().

notas = [5.0, 1.5, 9.0, 10.0, 6.6, 8.2]
soma_nota = 0
maior_nota = notas[0]
menor_nota = notas[0]
qtde_notas = len(notas)

for nota in notas:
    soma_nota += nota

media = soma_nota / qtde_notas

for nota in notas:
    if nota > maior_nota:
        maior_nota = nota
    if nota < menor_nota:
        menor_nota = nota

for i in range(qtde_notas):
    for j in range(0, qtde_notas - i - 1):
        if notas[j] > notas[j + 1]:
            notas[j], notas[j + 1] = notas[j + 1], notas[j]

print(f"Média da turma: {media:.2f}")
print(f"Maior nota: {maior_nota}")
print(f"Menor nota: {menor_nota}")
print(f"Notas ordenadas em ordem crescente: {notas}")
