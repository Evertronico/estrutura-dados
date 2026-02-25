def calcular_media(n1, n2):
    return (n1 + n2) / 2

def exibir_resultado(nome, media):
    print(f"Aluno: {nome}")
    print(f"Média: {media}")

nome = input("Nome: ")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = calcular_media(nota1, nota2)
exibir_resultado(nome, media)