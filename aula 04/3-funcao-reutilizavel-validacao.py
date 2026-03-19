def validar_aprovacao(media):
    if media >= 6:
        return "Aprovado"
    return "Reprovado"

def calcular_media(n1, n2):
    return (n1 + n2) / 2

media = calcular_media(7, 5)
situacao = validar_aprovacao(media)

print("Média:", media)
print("Situação:", situacao)