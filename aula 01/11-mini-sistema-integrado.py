nomes = []
notas = []

for i in range(3):
    nomes.append(input("Nome do aluno: "))
    notas.append(float(input("Nota do aluno: ")))

media = sum(notas) / len(notas)

print("Alunos:", nomes)
print("Média da turma:", media)
