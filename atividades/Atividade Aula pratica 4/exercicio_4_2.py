import modulo_avaliacao

nome_aluno = input("Nome do aluno: ")
curso_aluno = input("Curso matriculado: ")
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))

mensagem_final = modulo_avaliacao.avaliar_aluno(nome_aluno, curso_aluno, n1, n2)

print(mensagem_final)