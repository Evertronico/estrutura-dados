listaNotas = [1,2,3]

maior = 0
menor = 0
soma = 0



for nota in listaNotas:
    if maior == 0 and menor == 0:
        maior = nota
        menor = nota
        soma += nota
    else:
        if nota > maior:
            maior = nota
            soma += nota
        elif nota < menor:
            menor = nota
            soma += nota

media = 0
indexMaior = -1
indexMenor = -1

for i in range(len(listaNotas)):
    if listaNotas[i] == maior:
        indexMaior = i
    if listaNotas[i] == menor:
        indexMenor = i

#retirando número de index maior e menor

NotasDescartadas = []

NotasDescartadas.append(listaNotas.pop(indexMaior))
NotasDescartadas.append(listaNotas.pop(indexMenor))


media = soma/len(listaNotas)

print(media)
print(soma)
print(len(listaNotas))
print(maior)
print(menor)
print(listaNotas)
print(NotasDescartadas)
        