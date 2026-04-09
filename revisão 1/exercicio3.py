# lista ordenada inicial
lista = [10, 20, 30, 40]

# valor a inserir
valor = int(input("Digite o valor a ser inserido: "))

# encontra a posição correta (lógica de inserção)
pos = 0
while pos < len(lista) and lista[pos] < valor:
    pos += 1

# deslocamento manual doa elementos criando um espaço no final
lista.append(0)

# desloca os elementos
for i in range(len(lista) -1, pos, -1):
    lista[i] = lista[i - 1]

# insere o valor na posição correta
lista[pos] = valor

# exibe a lista atualizada
print("Lista atualizada:", lista)