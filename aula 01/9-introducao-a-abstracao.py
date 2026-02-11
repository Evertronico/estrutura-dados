# usamos a função sem nos preocupar com como ela calcula.
def calcular_media(lista):
    return sum(lista) / len(lista)

notas = [7, 8, 9]
print("Média:", calcular_media(notas))
