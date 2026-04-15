def inserir_ordenado(lista, valor):
    nova_lista = []
    for item in lista:
        nova_lista.append(item)
    nova_lista.append(0)  

    pos = 0
    while pos < len(lista) and lista[pos] < valor:
        pos += 1

    for i in range(len(nova_lista) - 1, pos, -1):
        nova_lista[i] = nova_lista[i - 1]
    nova_lista[pos] = valor

    return nova_lista

numeros = []

while True:
    valor = int(input("Digite um número (ou -1 para sair): "))

    if valor == -1:
        break

    numeros = inserir_ordenado(numeros, valor)
    print("Lista ordenada:", numeros)