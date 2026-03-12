# Lista de idades cadastradas
idades = [15, 18, 21, 16, 30, 14, 25]

maiores = []

for idade in idades:
    if idade >= 18:
        maiores.append(idade)

print("Lista original:", idades)
print("Maiores de idade:", maiores)