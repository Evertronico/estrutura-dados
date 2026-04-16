# Lista para armazenar notas (estrutura linear)
notas = []

# Entrada de dados (uso de repetição e input)
for i in range(5):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota) # inserção em lista

# Cálculo da média (uso de acumulador)
soma = 0
for nota in notas:
    soma += nota # soma dos elementos

media = soma / len(notas) # cálculo da média

# Encontrar maior valor (algoritmo manual)
maior = notas[0]
for nota in notas:
    if nota > maior:
        maior = nota

# Contar acima da média
acima = 0
for nota in notas:
    if nota > media:
        acima += 1

# Saída
print("Média:", media)
print("Maior nota:", maior)
print("Acima da média:", acima)