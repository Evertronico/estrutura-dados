nomes = []
notas = []


for i in range(3):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    
    nomes.append(nome)
    notas.append(nota)

media = sum(notas) / len(notas)
maior_nota = max(notas)
menor_nota = min(notas)


print("\n===== RESULTADOS =====")
print("Alunos registrados:", nomes)
print("Média da turma:", media)
print("Maior nota registrada:", maior_nota)
print("Menor nota registrada:", menor_nota)