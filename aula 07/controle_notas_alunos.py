# Lista representando notas de estudantes
notas = [7.5, 8.0, 6.5, 9.0, 5.5]

# Cálculo da média
soma = 0

for nota in notas:
    soma += nota

media = soma / len(notas)

print("Notas:", notas)
print("Média da turma:", media)