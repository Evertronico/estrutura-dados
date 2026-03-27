podrutos = ["Mouse", "teclado", "monitor"]

estoques = [10,3,5]

indice = -1

busca = "teclado"

for i in range(len(produtos)):
    if produto[i] == busca:
        indice = i
        break

if indice != -1:
    print("Produto encontrado: ", produtos[indice])
    print("Estoque: ", estoque[indice])
else:
    print("Produto não encontrado")

