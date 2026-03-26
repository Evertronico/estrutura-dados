# Atividade 1 - Remoção Manual
lista = [10, 20, 30, 40, 50]
indice_remover = 2 # Queremos tirar o 30

# Desloca todo mundo que está depois do 30 uma casa para a esquerda
for i in range(indice_remover, len(lista) - 1):
    lista[i] = lista[i + 1]

# "Diminui" a lista (corta o último que ficou duplicado)
lista[:] = lista[:-1]

print(f"Lista após remoção: {lista}")