# Lista ordenada inicial
lista = [10, 20, 30, 40]

# Valor a inserir
valor = int(input("Digite o valor: "))

# Encontrar posição correta (lógica de inserção)
pos = 0
while pos < len(lista) and lista[pos] < valor:
    pos += 1

# Deslocamento manual dos elementos
lista.append(0) # cria espaço no final

# desloca da direita para esquerda
for i in range(len(lista)-1, pos, -1):
    lista[i] = lista[i-1]

# insere valor na posição correta
lista[pos] = valor

# saída
print("Lista atualizada:", lista)