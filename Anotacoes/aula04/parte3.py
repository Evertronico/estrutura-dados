# Função para validar aprovação do aluno

def valide_aprovação(media):
    if(media < 6):
        print("Reprovado")
    else:
        print("aprovado")


# funcao apra calcular média

def calcule_media(n1,n2):
    return (n1,n2) / 2

# define notas, calcula medioa e determina situacao

media = calcule_media(7,5)
situacao = valide_aprovação(media)

print("Media: ", media)
print("Situação", situacao)