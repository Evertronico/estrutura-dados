'''
    Atividade Aula prática 1:
    Objetivo: demonstrar, por meio de um programa em Python, a compreensão dos conceitos de dado, informação, estrutura de dados, classificação das estruturas e abstração, utilizando entrada, processamento e saída de dados.
    Enunciado: Desenvolva um programa em Python que Solicite ao usuário:
     * O nome de 3 alunos
     * Uma nota para cada aluno
     * Armazene os dados utilizando uma estrutura de dados linear
    Calcule:
     * A média das notas
     * A maior nota
     * A menor nota
    Exiba as informações calculadas na tela
    Regra obrigatória: todo o código deve conter comentários explicativos, relacionando cada parte do programa aos conceitos estudados em aula.
'''

# Função de calculo da media (Abstração).
def calcular_media(Lnotas):
    return sum(Lnotas) / len(Lnotas)

# Estrutura de dados Linear.
nomes = []
notas = []

# Entrada de dados.    
for i in range(3):
    # Dados em conjunto com o Armazenamento.
    nomes.append(input(f"Nome do {i+1}° Aluno : "))
    notas.append(float(input(f"Nota do {i+1}° Aluno: ")))

    print('-'*30)

# Processamento de dados. 
media = calcular_media(notas)
maiorN = max(notas)
menorN = min(notas)

# Saida e Informação
print("=" *30)
print(f"Alunos: {nomes}")
print(f"Média da turma: {media:.2f}")
print(f"Maior nota da turma: {maiorN}")
print(f"Menor nota da turma: {menorN}")
