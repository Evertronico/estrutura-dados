# função de soma
def some(a, b):
    return a + b

# função de multiplicação
def muliplique(a, b):
    return a * b

# eleva ao quadrado
def eleve(a):
    return a * a

# recebe os dados
def receba_dados():
    nome = input("Informe seu nome: ")
    curso = input("Informe seu curso: ")
    nota1 = float(input("Digite sua primeira nota: "))
    nota2 = float(input("Digite sua segundaa nota: "))
    return nome, curso, nota1, nota2

def calcule_media(nota1, nota2):
    return (nota1 + nota2) / 2

    # valida a aprovação
def valide_aprovacao(media):
    if media >= 6:
        return "Aprovado"
    return "Reprovado"