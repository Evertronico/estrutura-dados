# Atividade 1 - Busca Sequencial
lista = [10, 25, 40, 55, 70, 85, 100]
procurado = 55
posicao = -1

for i in range(len(lista)):
    if lista[i] == procurado:
        posicao = i
        break # Para assim que achar

if posicao != -1:
    print(f"O valor {procurado} está na posição {posicao}")
else:
    print("Valor não encontrado.")