produtos = ["mouse", "teclado", "monitor", "impressora"]

estoques = [10, 5, 3, 2]

indice = -1
busca = "abobora"

#percorre a lista produtos
for i in range(len(produtos)):
    if produtos[i] == busca:
        indice = i
        break

if indice != -1:
    print("Produto encontrado: ", produtos[indice])
    print("Produtos em estoque: ", estoques[indice])
else:
    print("Produto " + busca + " não encontrado")