#lista de notas de alunos
notas = [7.5, 8.3, 9.2, 3.5, 2,7, 8.2, 3.4, 2.1, 9.0, 6.8]

#soma das notas
soma = 0

#agrega cada nota a soma
for nota in notas:
    soma += nota

#media das notas 
media = soma / len(notas)

print("Notas: ", notas)
print(f'Media da turma: {media:.2f}')