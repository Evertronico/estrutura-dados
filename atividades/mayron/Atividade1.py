notas = [7.5, 8.0, 6.5, 9.0, 5.5, 10.0, 4.5, 7.0, 8.5, 6.0]

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

tamanho = len(notas)
for i in range(tamanho):
    for j in range(0, tamanho - i - 1):
        if notas[j] > notas[j + 1]:
            notas[j], notas[j + 1] = notas[j + 1], notas[j]

print("Média da turma:", media)
print("Maior nota encontrada:", maior)
print("Menor nota encontrada:", menor)
print("Lista de notas ordenadas (crescente):", notas)