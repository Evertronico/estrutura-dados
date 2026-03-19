notas = []
# colocar notas
for i in range(10):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)
    
soma = 0
for nota in notas:
    soma = soma + nota    
media = soma / len(notas)

maior = notas[0]
menor = notas[0]

# ordenação das notas
for nota in notas:
    if nota > maior:
        maior = nota
    elif nota < menor:
        menor = nota    
ordem = notas[:]

for i in range(len(ordem)):
    for p in range(len(ordem) - 1):
        if ordem[p] > ordem[p +1]:
            temp = ordem[p]
            ordem[p] = ordem[p + 1]
            ordem[p + 1] = temp
            
            
# ecibição das notas            
print("Média: ", media)
print("Maior nota: ", maior)
print("Menor nota: ", menor)
print("Notas em ordem: ", ordem)
        