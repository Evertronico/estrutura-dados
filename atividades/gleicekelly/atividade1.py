# Atividade 1 — Estatísticas de Notas
# Crie um programa que armazene 10 notas de alunos em uma lista.
# O programa deve calcular e exibir:
# média da turma
# maior nota
# menor nota
# lista de notas ordenadas em ordem crescente
# Não utilize a função sort().

notas = [9.5, 10.0, 2.5, 5.5, 7.5, 6.7, 8.5, 9.0, 8.0, 7.0]

soma = 0

for nota in notas:
    soma += nota

media = soma / len(notas)

print("A media das notas: ", media)

maior = notas[0] 
menor = notas[0]

maiorNota = 0
menorNota = 0

for i in range(len(notas)):
    if notas[i] > maior:
        maior = notas[i]
        maiorNota = i

    if notas[i] < menor:
        menor = notas[i]
        menorNota = i

print("A maior nota: ", maior)        
print("A menor nota: ", menor)

n = len(notas)

for i in range(n):
    for j in range(0, n-i-1):
        if notas[j] > notas[j+1]:
            notas[j], notas[j+1] = notas[j+1], notas[j]

print("Lista de notas ordenadas: ", notas)