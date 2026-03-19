def inserir(lista, valor):
    nova = []
    inserido = False

    for item in lista:
        if not inserido and valor < item:
            nova.append(valor)
            inserido = True
        nova.append(item)


        if not inserido:
            nova.append(valor)


        return nova