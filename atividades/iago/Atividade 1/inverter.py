# Atividade 1 - Inverter Lista Manualmente
lista = [1, 2, 3, 4, 5]
lista_invertida = []

# Percorre do último para o primeiro
for i in range(len(lista) - 1, -1, -1):
    lista_invertida[:] = lista_invertida + [lista[i]]

print(f"Original: {lista}")
print(f"Invertida: {lista_invertida}")