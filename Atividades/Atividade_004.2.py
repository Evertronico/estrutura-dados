'''
--problema na importação
Atividade Aula prática 4:
    Exercício 4.2
    Crie uma função que receba nome, curso e duas notas e retorne uma mensagem formatada
    informando que o {nome} matriculado no curso {curso} está {“Aprovado”|”Reprovado”},
    essa implementação deve se dar por meio de um módulo.  
'''
from aula04.operacoes import aprovacao

print("=" * 50)
print("SISTEMA DE MATRÍCULA E NOTAS")
print("-" * 50)

nome_aluno = input("Nome do aluno: ")
nome_curso = input("Nome do curso: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

resultado_final = aprovacao(nome_aluno,nome_curso,nota1,nota2)

print("=" * 50)
print(resultado_final)
print("=" * 50)
