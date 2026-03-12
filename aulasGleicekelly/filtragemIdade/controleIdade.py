idades = [25, 30, 22, 28, 35, 12, 16, 24, 37, 11, 6, 97]

maiores = []

for idade in idades:
    #verifica se idade > 18
    if idade >= 18:
        maiores.append(idade)

#exibe todas as idades
print("Idades: ", idades)
print("Idades maiores de 18: ", maiores)