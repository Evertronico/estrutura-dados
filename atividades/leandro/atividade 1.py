notas = []
total = 0

for x in range(5):
    notas.append(float(input(f"Informe a {x+1}ª nota: ")))
    
maior_nota = menor_nota = notas[0]

for num in notas:
    total += num
    if num > maior_nota:
        maior_nota = num
    if num < menor_nota:
        menor_nota = num

for x in range(len(notas)-1, 0 ,-1):
    for y in range(x):
        if notas[y] > notas[y+1]:
            notas[y], notas[y+1] = notas[y+1], notas[y]

print("")
print(f"A maior nota é: {maior_nota}")
print(f"A menor nota é: {menor_nota}")
print(f"A média das notas foi: {total/len(notas)}")
print("")
print("Lista em ordem crescente")
print(notas)