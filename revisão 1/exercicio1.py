# lista para armazenar notas (estrutura linear)
notas = []

# entrada de dados (uso de repetição e input)
for i in range(5):
    # recebe a nota informada
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    # adiciona a nota ao vetor ou array
    notas.append(nota)

# cálculo da média (uso de acumulador)
soma = 0
for nota in notas:
    # para cada nota, acumula o valor na variável soma
    soma += nota

# cálculo da média
media = soma / len(notas)

# encontrar a maior nota
maior = notas[0]
for nota in notas:
    if nota > maior:
        maior = nota

# contar notas acima da média
acima = 0
for nota in notas:
    if nota > media:
        acima += 1

# exibição dos resultados
print(f"Média das notas: {media:.2f}")
print(f"Maior nota: {maior:.2f}")
print(f"Quantidade de alunos com nota acima da média: {acima}")