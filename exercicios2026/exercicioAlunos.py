#importando a função de outro arquivo
import mediaAlunos

#lista para nomes e notas dos alunos
nomes = []
notas = []

for i in range(3):
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    nota = float(input(f"Digite a nota do {nome}: "))

    nomes.append(nome)
    notas.append(nota)

#calculando a media dos alunos com indices
media = mediaAlunos.calcular_media(notas[0], notas[1], notas[2])
maior_nota = max(notas)
menor_nota = min(notas)

#mostrando na tela os resultados
print(f"Nomes dos alunos: {nomes}")
print("Notas: ", notas)
print(f"Média da turma: {media:.2f}")
print(f"Maior nota: {maior_nota}")
print(f"Menor nota: {menor_nota}")