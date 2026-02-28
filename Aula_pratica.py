Aluno = [] # Lista para armazenar os nomes dos alunos
Nota = [] # Lista para armazenar as notas dos alunos

# Pede ao usuário para inserir os nomes dos alunos e suas notas
Aluno.append(input("Digite o nome do aluno: ")) # Adiciona o nome do aluno à lista Aluno
Aluno.append(input("Digite o nome do aluno: ")) # Adiciona o nome do aluno à lista Aluno
Aluno.append(input("Digite o nome do aluno: ")) # Adiciona o nome do aluno à lista Aluno
Nota.append(float(input("Digite a nota do aluno: "))) # Adiciona a nota do aluno à lista Nota
Nota.append(float(input("Digite a nota do aluno: ")))  # Adiciona a nota do aluno à lista Nota
Nota.append(float(input("Digite a nota do aluno: "))) # Adiciona a nota do aluno à lista Nota
 
# Calcula a média, a nota mais alta e a nota mais baixa
media = (Nota[0] + Nota[1] + Nota[2]) / 3 # Calcula a média das notas dos alunos
nota_alta = max(Nota) # Encontra a nota mais alta na lista Nota
nota_baixa = min(Nota) # Encontra a nota mais baixa na lista Nota

# Imprime os resultados
print(f"A média das notas dos alunos é: {media}") # Imprime a média das notas dos alunos
print(f"A nota mais alta é: {nota_alta}") # Imprime a nota mais alta
print(f"A nota mais baixa é: {nota_baixa}") # Imprime a nota mais baixa
