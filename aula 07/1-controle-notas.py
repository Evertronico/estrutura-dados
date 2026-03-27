notas = [7.5,8.3,9.2,3.5,2.7,8.2,4.3]

#soma de todoas as notas

soma = 0

for nota in notas:
    soma += nota

media = soma/ len(notas)

print("Notas: ", notas)
print(f'Media da turma: {media:.2f}')