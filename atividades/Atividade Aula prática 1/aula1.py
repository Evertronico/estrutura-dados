nomes = []
notas = []

for i in range(3):
    nomes.append(input("Nome do aluno: "))
    notas.append(float(input("Nota do aluno: ")))

def calcular_media(lista_notas):
    
    return sum(lista_notas) / len(lista_notas)

def encontrar_maior(lista_notas):
    
    return max(lista_notas)

def encontrar_menor(lista_notas):
    
    return min(lista_notas)

media = calcular_media(notas)
maior_nota = encontrar_maior(notas)
menor_nota = encontrar_menor(notas)

print("------")
print("Alunos registrados:", nomes)
print("Média da turma:", media)
print("Maior nota registrada:", maior_nota)
print("Menor nota registrada:", menor_nota)