'''
    Atividade 1 — Estatísticas de Notas
    Crie um programa que armazene 10 notas de alunos em uma lista.
    O programa deve calcular e exibir:
    média da turma
    maior nota
    menor nota
    lista de notas ordenadas em ordem crescente
    Não utilize a função sort().
'''
notas = [7.5, 8.0, 6.5, 9.0, 5.5, 10, 5.1, 9.5, 7.5, 0.1]

soma = 0
maior = notas[0]
menor = notas[0]

for nota in notas:
    soma += nota
    if nota > maior:
        maior = nota
    if nota < menor:
        menor = nota

media = soma / len(notas)


notasL = notas[:]  
n = len(notasL)

for i in range(n):
    for a in range(0, n-i-1):
        if notasL[a] > notasL[a+1]:
            notasL[a], notasL[a+1] = notasL[a+1], notasL[a]


print(f"Média da turma: {media:.2f}")
print("Maior nota:", maior)
print("Menor nota:", menor)
print("Notas ordenadas:", notasL)
