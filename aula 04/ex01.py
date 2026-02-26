import operacoes

nome = input('Nome do aluno: ')
curso = input('Curso: ')
nota1 = float(input('Primeira nota de {aluno}: '))
nota2 = float(input('Segunda nota de {aluno}: '))

print(operacoes.exiba_result_aluno(nome, curso, nota1, nota2))