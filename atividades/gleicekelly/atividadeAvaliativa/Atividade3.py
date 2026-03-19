def inserir_ordenado(lista, valor):
    posicao = 0
    while posicao < len(lista) and lista[posicao] < valor:
        posicao += 1

    lista.append(None)

    for i in range(len(lista) - 1, posicao, -1):
        lista[i] = lista[i - 1]

    lista[posicao] = valor
    return lista

dados = []
valores_para_inserir = [45, 12, 89, 2, 33]

print("Inserindo dados um a um:")
for v in valores_para_inserir:
    inserir_ordenado(dados, v)
    print(f"Inserido {v:2d} -> Lista: {dados}")