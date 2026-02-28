def principal ():
     aluno = input("Digite o nome do aluno: ")
     curso = input("Digite o nome do curso: ")
     nota1 = float(input("Digite a primeira nota: "))
     nota2 = float(input("Digite a segunda nota: "))

     media = (nota1 + nota2) / 2

     if media >= 6:
           media = "aprovado"
     else:
          media = "reprovado"

     print(f"O aluno {aluno} do curso de {curso} esta {media}")

principal()