# Atividade 1 — Estatísticas de Notas
# Crie um programa que armazene 10 notas de alunos em uma lista.
# O programa deve calcular e exibir:
# média da turma
# maior nota
# menor nota
# lista de notas ordenadas em ordem crescente
# Não utilize a função sort().

# ========================
def calcular_soma(lista):
    total = 0
    for nota in lista:
        total+=nota
    return total
# ========================
def organiza(lista):
    for i in range(len(lista) -1, 0, -1):
        for j in range(i):
            if lista[j] > lista[j+1]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp

# ========================
def maior(lista):
    return lista[len(lista)-1]
# ========================
def menor(lista):
    return lista[0]
# ========================
def media(lista):
    somaTotal = calcular_soma(lista)
    return somaTotal/ len(lista)
# ========================


notas = []
soma = 0

for i in range(3):
    num = int(input('Informe nota : '))
    notas.append(num)

organiza(notas)
media_nota = media(notas)
print(f'A média da turma é {media_nota}')
menor_nota = menor(notas)
print(f'A menor nota é {menor_nota}')
maior_nota = maior(notas)
print(f'A maior nota é {maior_nota}')
print(notas)

